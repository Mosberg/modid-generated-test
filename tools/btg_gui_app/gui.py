from __future__ import annotations

import queue
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox, ttk
from typing import List, Optional, Sequence, Tuple

from .commands import BTGCommandMixin
from .config_store import ConfigStoreMixin
from .runner import ProcessRunner
from .util import (
    find_repo_root,
    format_cmd,
    guess_btg_script,
    now_ts,
    open_in_file_manager,
    try_rel,
)


APP_NAME = "BTG GUI"
APP_VERSION = "2.0.0"
DEFAULT_GEOMETRY = "1120x820"


class BTGGui(ttk.Frame, BTGCommandMixin, ConfigStoreMixin):
    def __init__(self, master: tk.Tk) -> None:
        super().__init__(master)
        self.master = master

        # Async output queue -> polled by Tk.
        self._log_q: "queue.Queue[str]" = queue.Queue()

        # Persistent config + project paths.
        self.repo_root = tk.StringVar(value=str(find_repo_root(Path.cwd())))
        self.btg_script = tk.StringVar(value="")
        self.python_exe = tk.StringVar(value=str(Path(getattr(__import__("sys"), "executable")).resolve()))

        # Global flags
        self.log_level = tk.StringVar(value="INFO")
        self.global_dry_run = tk.BooleanVar(value=False)

        # Tabs vars
        self.val_schemas = tk.StringVar(value="schemas")
        self.val_palettes = tk.StringVar(value="palettes")

        self.norm_palettes = tk.StringVar(value="palettes")

        self.ext_textures = tk.StringVar(value="textures")
        self.ext_palettes_out = tk.StringVar(value="palettes")
        self.ext_max_colors = tk.StringVar(value="32")
        self.ext_min_alpha = tk.StringVar(value="1")
        self.ext_schema_ref = tk.StringVar(value="../../schemas/texture-palettes.schema.json")
        self.ext_generator_version = tk.StringVar(value="1.0.0")

        self.rec_palettes_dir = tk.StringVar(value="palettes")
        self.rec_src_palette = tk.StringVar(value="wood/oak.texture-palettes.json")
        self.rec_dst_palette = tk.StringVar(value="metal/iron.texture-palettes.json")
        self.rec_src_id = tk.StringVar(value="oak")
        self.rec_dst_id = tk.StringVar(value="iron")
        self.rec_group = tk.StringVar(value="")
        self.rec_input = tk.StringVar(value="textures_input")
        self.rec_output = tk.StringVar(value="output/textures/item")
        self.rec_no_recursive = tk.BooleanVar(value=False)
        self.rec_min_alpha = tk.StringVar(value="1")
        self.rec_alpha_weight = tk.StringVar(value="0.25")
        self.rec_preserve_alpha = tk.BooleanVar(value=True)
        self.rec_exact_first = tk.BooleanVar(value=True)

        self.leg_palettes_dir = tk.StringVar(value="palettes")
        self.leg_templates_dir = tk.StringVar(value="textures_input")
        self.leg_output_root = tk.StringVar(value="output")
        self.leg_namespace = tk.StringVar(value="modid")
        self.leg_lang_file = tk.StringVar(value="en_us.json")
        self.leg_no_modid_tree = tk.BooleanVar(value=False)
        self.leg_no_flat_tree = tk.BooleanVar(value=False)

        self.gen_templates = tk.StringVar(value="textures_input")
        self.gen_palettes = tk.StringVar(value="palettes")
        self.gen_output = tk.StringVar(value="output/textures/item")
        self.gen_min_alpha = tk.StringVar(value="1")
        self.gen_alpha_weight = tk.StringVar(value="0.25")
        self.gen_preserve_alpha = tk.BooleanVar(value=True)
        self.gen_exact_first = tk.BooleanVar(value=True)
        self.gen_limit = tk.StringVar(value="")

        self.at_templates = tk.StringVar(value="textures_input")
        self.at_palettes = tk.StringVar(value="palettes")
        self.at_out_dir = tk.StringVar(value="")
        self.at_materials = tk.StringVar(value="wood,metal,glass")
        self.at_min_alpha = tk.StringVar(value="1")
        self.at_min_hits = tk.StringVar(value="2")

        self.as_textures = tk.StringVar(value="output/textures/item")
        self.as_recursive = tk.BooleanVar(value=False)
        self.as_items_dir = tk.StringVar(value="output/items")
        self.as_models_dir = tk.StringVar(value="output/models/item")
        self.as_lang = tk.StringVar(value="output/lang/en_us.json")
        self.as_namespace = tk.StringVar(value="modid")
        self.as_overwrite_lang = tk.BooleanVar(value=False)

        # Command preview + status
        self.status_var = tk.StringVar(value="Ready.")
        self.cmd_preview = tk.StringVar(value="")

        self._init_btg_path()
        self._build_ui()
        self.load_config_best_effort()
        self._refresh_cmd_preview()

        self._runner = ProcessRunner(self._log_q, self.status_var.set)
        self.after(75, self._poll_logs)

    # -------------------------
    # UI shell
    # -------------------------

    def _build_ui(self) -> None:
        self.master.title(f"{APP_NAME} {APP_VERSION}")
        self.master.geometry(DEFAULT_GEOMETRY)

        style = ttk.Style()
        try:
            style.theme_use("clam")
        except Exception:
            pass

        self.pack(fill="both", expand=True)

        self._build_menubar()

        top = ttk.LabelFrame(self, text="Project", padding=10)
        top.pack(fill="x", padx=10, pady=10)

        self._row_dir(top, 0, "Repo root:", self.repo_root, browse_title="Select repo root")
        self._row_file(
            top,
            1,
            "btg.py script:",
            self.btg_script,
            browse_title="Select btg.py",
            filetypes=[("Python", "*.py"), ("All files", "*.*")],
        )
        self._row_file(
            top,
            2,
            "Python exe:",
            self.python_exe,
            browse_title="Select Python executable",
            filetypes=[("Executables", "*.*")],
        )

        flags = ttk.Frame(top)
        flags.grid(row=3, column=0, columnspan=3, sticky="w", pady=(8, 0))

        ttk.Label(flags, text="Log level:").pack(side="left")
        ttk.Combobox(
            flags,
            textvariable=self.log_level,
            values=["DEBUG", "INFO", "WARNING", "ERROR"],
            width=10,
            state="readonly",
        ).pack(side="left", padx=(6, 14))

        ttk.Checkbutton(flags, text="Global dry-run", variable=self.global_dry_run).pack(side="left")

        ttk.Button(flags, text="Save Config", command=self.save_config).pack(side="left", padx=(16, 6))
        ttk.Button(flags, text="Reload Config", command=self.load_config_best_effort).pack(side="left")

        nb = ttk.Notebook(self)
        nb.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        self.tab_validate = ttk.Frame(nb)
        self.tab_normalize = ttk.Frame(nb)
        self.tab_extract = ttk.Frame(nb)
        self.tab_recolor = ttk.Frame(nb)
        self.tab_legacy = ttk.Frame(nb)
        self.tab_generate = ttk.Frame(nb)
        self.tab_autotemplate = ttk.Frame(nb)
        self.tab_assets = ttk.Frame(nb)

        nb.add(self.tab_validate, text="Validate")
        nb.add(self.tab_normalize, text="Normalize")
        nb.add(self.tab_extract, text="Extract")
        nb.add(self.tab_recolor, text="Recolor")
        nb.add(self.tab_legacy, text="Legacy Templates")
        nb.add(self.tab_generate, text="Generate")
        nb.add(self.tab_autotemplate, text="AutoTemplate")
        nb.add(self.tab_assets, text="Assets")

        self._build_validate_tab()
        self._build_normalize_tab()
        self._build_extract_tab()
        self._build_recolor_tab()
        self._build_legacy_tab()
        self._build_generate_tab()
        self._build_autotemplate_tab()
        self._build_assets_tab()

        runbar = ttk.LabelFrame(self, text="Run", padding=10)
        runbar.pack(fill="x", padx=10, pady=(0, 10))

        ttk.Label(runbar, text="Command preview:").grid(row=0, column=0, sticky="w")
        ttk.Entry(runbar, textvariable=self.cmd_preview, state="readonly").grid(
            row=1, column=0, columnspan=4, sticky="we", pady=(6, 0)
        )
        runbar.columnconfigure(0, weight=1)

        ttk.Button(runbar, text="Run Preview (Validate)", command=self.run_preview).grid(
            row=2, column=0, sticky="w", pady=(10, 0)
        )
        ttk.Button(runbar, text="Stop", command=self.stop).grid(
            row=2, column=1, sticky="w", padx=(10, 0), pady=(10, 0)
        )
        ttk.Button(runbar, text="Clear Output", command=self.clear_output).grid(
            row=2, column=2, sticky="w", padx=(10, 0), pady=(10, 0)
        )

        bottom = ttk.LabelFrame(self, text="Output", padding=10)
        bottom.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        self.log_text = tk.Text(bottom, height=16, wrap="word")
        self.log_text.pack(fill="both", expand=True)

        ttk.Label(self, textvariable=self.status_var, anchor="w").pack(fill="x", padx=10, pady=(0, 8))

        # Recompute preview command whenever a relevant var changes.
        for v in (
            self.repo_root,
            self.btg_script,
            self.python_exe,
            self.log_level,
            self.global_dry_run,
            self.val_schemas,
            self.val_palettes,
            self.norm_palettes,
            self.ext_textures,
            self.ext_palettes_out,
            self.ext_max_colors,
            self.ext_min_alpha,
            self.ext_schema_ref,
            self.ext_generator_version,
            self.rec_palettes_dir,
            self.rec_src_palette,
            self.rec_dst_palette,
            self.rec_src_id,
            self.rec_dst_id,
            self.rec_group,
            self.rec_input,
            self.rec_output,
            self.rec_no_recursive,
            self.rec_min_alpha,
            self.rec_alpha_weight,
            self.rec_preserve_alpha,
            self.rec_exact_first,
            self.leg_palettes_dir,
            self.leg_templates_dir,
            self.leg_output_root,
            self.leg_namespace,
            self.leg_lang_file,
            self.leg_no_modid_tree,
            self.leg_no_flat_tree,
            self.gen_templates,
            self.gen_palettes,
            self.gen_output,
            self.gen_min_alpha,
            self.gen_alpha_weight,
            self.gen_preserve_alpha,
            self.gen_exact_first,
            self.gen_limit,
            self.at_templates,
            self.at_palettes,
            self.at_out_dir,
            self.at_materials,
            self.at_min_alpha,
            self.at_min_hits,
            self.as_textures,
            self.as_recursive,
            self.as_items_dir,
            self.as_models_dir,
            self.as_lang,
            self.as_namespace,
            self.as_overwrite_lang,
        ):
            try:
                v.trace_add("write", lambda *_: self._refresh_cmd_preview())
            except Exception:
                pass

    def _build_menubar(self) -> None:
        mb = tk.Menu(self.master)

        filem = tk.Menu(mb, tearoff=False)
        filem.add_command(label="Save Config", command=self.save_config)
        filem.add_command(label="Save Config As…", command=self.save_config_as)
        filem.add_command(label="Reload Config", command=self.load_config_best_effort)
        filem.add_separator()
        filem.add_command(label="Exit", command=self.master.destroy)
        mb.add_cascade(label="File", menu=filem)

        toolsm = tk.Menu(mb, tearoff=False)
        toolsm.add_command(label="Open Repo Root", command=lambda: self._open_path(self.repo_root.get()))
        toolsm.add_command(label="Open Output Folder", command=self.open_output_folder)
        toolsm.add_separator()
        toolsm.add_command(label="Copy Preview Command", command=self.copy_preview_command)
        mb.add_cascade(label="Tools", menu=toolsm)

        helpm = tk.Menu(mb, tearoff=False)
        helpm.add_command(label="About", command=self.about)
        mb.add_cascade(label="Help", menu=helpm)

        self.master.config(menu=mb)

    # -------------------------
    # Small UI helpers
    # -------------------------

    def _row_dir(self, parent: ttk.Frame, row: int, label: str, var: tk.StringVar, *, browse_title: str) -> None:
        ttk.Label(parent, text=label).grid(row=row, column=0, sticky="w")
        ttk.Entry(parent, textvariable=var, width=80).grid(row=row, column=1, sticky="we", padx=8)
        ttk.Button(parent, text="Browse…", command=lambda: self._browse_dir(var, title=browse_title)).grid(
            row=row, column=2, sticky="w"
        )
        parent.columnconfigure(1, weight=1)

    def _row_file(
        self,
        parent: ttk.Frame,
        row: int,
        label: str,
        var: tk.StringVar,
        *,
        browse_title: str,
        filetypes: List[Tuple[str, str]],
    ) -> None:
        ttk.Label(parent, text=label).grid(row=row, column=0, sticky="w")
        ttk.Entry(parent, textvariable=var, width=80).grid(row=row, column=1, sticky="we", padx=8)
        ttk.Button(
            parent,
            text="Browse…",
            command=lambda: self._browse_file(var, title=browse_title, filetypes=filetypes),
        ).grid(row=row, column=2, sticky="w")
        parent.columnconfigure(1, weight=1)

    def _row_text(self, parent: ttk.Frame, row: int, label: str, var: tk.StringVar, *, width: int = 70) -> None:
        ttk.Label(parent, text=label).grid(row=row, column=0, sticky="w")
        ttk.Entry(parent, textvariable=var, width=width).grid(row=row, column=1, sticky="w", padx=8)

    # -------------------------
    # Tabs
    # -------------------------

    def _build_validate_tab(self) -> None:
        f = ttk.Frame(self.tab_validate, padding=10)
        f.pack(fill="x")
        self._row_dir(f, 0, "Schemas dir:", self.val_schemas, browse_title="Select schemas directory")
        self._row_dir(f, 1, "Palettes dir:", self.val_palettes, browse_title="Select palettes directory")
        ttk.Button(f, text="Run Validate", command=self.run_validate).grid(row=2, column=0, sticky="w", pady=(10, 0))

    def _build_normalize_tab(self) -> None:
        f = ttk.Frame(self.tab_normalize, padding=10)
        f.pack(fill="x")
        self._row_dir(f, 0, "Palettes dir:", self.norm_palettes, browse_title="Select palettes directory")
        ttk.Button(f, text="Run Normalize", command=self.run_normalize).grid(row=1, column=0, sticky="w", pady=(10, 0))

    def _build_extract_tab(self) -> None:
        f = ttk.Frame(self.tab_extract, padding=10)
        f.pack(fill="x")
        self._row_dir(f, 0, "Textures dir:", self.ext_textures, browse_title="Select textures directory")
        self._row_dir(f, 1, "Palettes output dir:", self.ext_palettes_out, browse_title="Select output palettes directory")
        self._row_text(f, 2, "Max colors:", self.ext_max_colors, width=12)
        self._row_text(f, 3, "Min alpha:", self.ext_min_alpha, width=12)
        self._row_text(f, 4, "$schema ref:", self.ext_schema_ref, width=70)
        self._row_text(f, 5, "Generator version:", self.ext_generator_version, width=18)
        ttk.Button(f, text="Run Extract", command=self.run_extract).grid(row=6, column=0, sticky="w", pady=(10, 0))

    def _build_recolor_tab(self) -> None:
        f = ttk.Frame(self.tab_recolor, padding=10)
        f.pack(fill="x")
        self._row_dir(f, 0, "Palettes dir:", self.rec_palettes_dir, browse_title="Select palettes directory")
        self._row_text(f, 1, "Source palette (rel):", self.rec_src_palette, width=70)
        self._row_text(f, 2, "Target palette (rel):", self.rec_dst_palette, width=70)
        self._row_text(f, 3, "Source id:", self.rec_src_id, width=20)
        self._row_text(f, 4, "Target id:", self.rec_dst_id, width=20)
        self._row_text(f, 5, "Group (blank=auto):", self.rec_group, width=20)
        self._row_dir(f, 6, "Input dir:", self.rec_input, browse_title="Select input directory")
        self._row_dir(f, 7, "Output dir:", self.rec_output, browse_title="Select output directory")
        ttk.Checkbutton(f, text="No recursive input scan", variable=self.rec_no_recursive).grid(
            row=8, column=0, sticky="w", pady=(10, 0)
        )
        self._row_text(f, 9, "Min alpha:", self.rec_min_alpha, width=12)
        self._row_text(f, 10, "Alpha weight:", self.rec_alpha_weight, width=12)
        ttk.Checkbutton(f, text="Preserve original alpha", variable=self.rec_preserve_alpha).grid(
            row=11, column=0, sticky="w", pady=(8, 0)
        )
        ttk.Checkbutton(f, text="Exact-match first", variable=self.rec_exact_first).grid(
            row=12, column=0, sticky="w", pady=(6, 0)
        )
        ttk.Button(f, text="Run Recolor", command=self.run_recolor).grid(row=13, column=0, sticky="w", pady=(10, 0))

    def _build_legacy_tab(self) -> None:
        f = ttk.Frame(self.tab_legacy, padding=10)
        f.pack(fill="x")
        self._row_dir(f, 0, "Palettes dir:", self.leg_palettes_dir, browse_title="Select palettes directory")
        self._row_dir(f, 1, "Templates dir:", self.leg_templates_dir, browse_title="Select templates directory")
        self._row_dir(f, 2, "Output root:", self.leg_output_root, browse_title="Select output root directory")
        self._row_text(f, 3, "Namespace/modid:", self.leg_namespace, width=20)
        self._row_text(f, 4, "Lang file:", self.leg_lang_file, width=20)
        ttk.Checkbutton(f, text="Disable output//... tree", variable=self.leg_no_modid_tree).grid(
            row=5, column=0, sticky="w", pady=(10, 0)
        )
        ttk.Checkbutton(f, text="Disable flat output/... tree", variable=self.leg_no_flat_tree).grid(
            row=6, column=0, sticky="w", pady=(6, 0)
        )
        ttk.Button(f, text="Run Legacy recolor-templates", command=self.run_legacy_templates).grid(
            row=7, column=0, sticky="w", pady=(10, 0)
        )

    def _build_generate_tab(self) -> None:
        f = ttk.Frame(self.tab_generate, padding=10)
        f.pack(fill="x")
        self._row_dir(f, 0, "Templates dir:", self.gen_templates, browse_title="Select templates directory")
        self._row_dir(f, 1, "Palettes dir:", self.gen_palettes, browse_title="Select palettes directory")
        self._row_dir(f, 2, "Output dir:", self.gen_output, browse_title="Select output directory")
        self._row_text(f, 3, "Min alpha:", self.gen_min_alpha, width=12)
        self._row_text(f, 4, "Alpha weight:", self.gen_alpha_weight, width=12)
        self._row_text(f, 5, "Limit (blank=none):", self.gen_limit, width=12)
        ttk.Checkbutton(f, text="Preserve alpha", variable=self.gen_preserve_alpha).grid(
            row=6, column=0, sticky="w", pady=(10, 0)
        )
        ttk.Checkbutton(f, text="Exact-match first", variable=self.gen_exact_first).grid(
            row=7, column=0, sticky="w", pady=(6, 0)
        )
        ttk.Button(f, text="Run Generate", command=self.run_generate).grid(row=8, column=0, sticky="w", pady=(10, 0))

    def _build_autotemplate_tab(self) -> None:
        f = ttk.Frame(self.tab_autotemplate, padding=10)
        f.pack(fill="x")
        self._row_dir(f, 0, "Templates dir (*.png):", self.at_templates, browse_title="Select templates directory")
        self._row_dir(f, 1, "Palettes dir:", self.at_palettes, browse_title="Select palettes directory")
        self._row_text(f, 2, "Out dir (blank=templates):", self.at_out_dir, width=70)
        self._row_text(f, 3, "Materials (comma list):", self.at_materials, width=70)
        self._row_text(f, 4, "Min alpha:", self.at_min_alpha, width=12)
        self._row_text(f, 5, "Min hits:", self.at_min_hits, width=12)
        ttk.Button(f, text="Run AutoTemplate", command=self.run_autotemplate).grid(
            row=6, column=0, sticky="w", pady=(10, 0)
        )

    def _build_assets_tab(self) -> None:
        f = ttk.Frame(self.tab_assets, padding=10)
        f.pack(fill="x")
        self._row_dir(f, 0, "Textures dir:", self.as_textures, browse_title="Select textures directory")
        ttk.Checkbutton(f, text="Recurse textures dir", variable=self.as_recursive).grid(row=1, column=0, sticky="w", pady=(6, 0))
        self._row_dir(f, 2, "Items dir:", self.as_items_dir, browse_title="Select items output directory")
        self._row_dir(f, 3, "Models/item dir:", self.as_models_dir, browse_title="Select models output directory")
        self._row_text(f, 4, "Lang file:", self.as_lang, width=70)
        self._row_text(f, 5, "Namespace/modid:", self.as_namespace, width=20)
        ttk.Checkbutton(f, text="Overwrite existing lang keys", variable=self.as_overwrite_lang).grid(
            row=6, column=0, sticky="w", pady=(10, 0)
        )
        ttk.Button(f, text="Run Assets", command=self.run_assets).grid(row=7, column=0, sticky="w", pady=(10, 0))

    # -------------------------
    # Browse helpers
    # -------------------------

    def _browse_dir(self, var: tk.StringVar, *, title: str) -> None:
        start = self._abs_repo()
        p = filedialog.askdirectory(title=title, initialdir=str(start))
        if not p:
            return
        repo = self._abs_repo()
        var.set(try_rel(repo, Path(p)))
        self._maybe_update_btg_guess()

    def _browse_file(self, var: tk.StringVar, *, title: str, filetypes: List[Tuple[str, str]]) -> None:
        start = self._abs_repo()
        p = filedialog.askopenfilename(title=title, initialdir=str(start), filetypes=filetypes)
        if not p:
            return
        repo = self._abs_repo()
        var.set(try_rel(repo, Path(p)))
        self._maybe_update_btg_guess()

    # -------------------------
    # Run actions
    # -------------------------

    def run_validate(self) -> None:
        self._run(self._cmd_validate(), label="validate")

    def run_normalize(self) -> None:
        self._run(self._cmd_normalize(), label="normalize")

    def run_extract(self) -> None:
        self._run(self._cmd_extract(), label="extract")

    def run_recolor(self) -> None:
        self._run(self._cmd_recolor(), label="recolor")

    def run_legacy_templates(self) -> None:
        self._run(self._cmd_legacy_templates(), label="recolor-templates")

    def run_generate(self) -> None:
        self._run(self._cmd_generate(), label="generate")

    def run_autotemplate(self) -> None:
        self._run(self._cmd_autotemplate(), label="autotemplate")

    def run_assets(self) -> None:
        self._run(self._cmd_assets(), label="assets")

    def run_preview(self) -> None:
        # Keep preview safe: run validate.
        self._run(self._cmd_validate(), label="preview(validate)")

    # -------------------------
    # Command preview
    # -------------------------

    def _refresh_cmd_preview(self) -> None:
        argv = self._compose_full_command(self._cmd_validate())
        self.cmd_preview.set(format_cmd(argv))

    def _compose_full_command(self, btg_argv: List[str]) -> List[str]:
        py = self._abs_python_exe()
        btg = self._abs_btg_script()
        out = [str(py), str(btg)]
        out.extend(self._global_args())
        out.extend(btg_argv)
        return [str(x) for x in out]

    # -------------------------
    # Process execution
    # -------------------------

    def _run(self, btg_argv: List[str], *, label: str) -> None:
        if self._runner.running:
            messagebox.showwarning("Busy", "A task is already running. Stop it first.")
            return

        repo = self._abs_repo()
        btg = self._abs_btg_script()
        py = self._abs_python_exe()

        if not repo.exists():
            messagebox.showerror("Invalid repo", "Repo root does not exist.")
            return
        if not btg.exists():
            messagebox.showerror("Missing btg.py", f"btg.py not found: {btg.as_posix()}")
            return
        if not py.exists():
            messagebox.showerror("Missing Python", f"Python executable not found: {py.as_posix()}")
            return

        full = self._compose_full_command(btg_argv)
        self._log(f"[{now_ts()}] INFO: Running ({label}): {format_cmd(full)}")
        self._log(f"[{now_ts()}] INFO: cwd: {repo.as_posix()}")
        self._runner.start(full, cwd=repo, label=label)

    def stop(self) -> None:
        self._runner.stop()

    # -------------------------
    # Logging
    # -------------------------

    def _log(self, msg: str) -> None:
        try:
            self._log_q.put_nowait(msg)
        except Exception:
            pass

    def _poll_logs(self) -> None:
        try:
            while True:
                line = self._log_q.get_nowait()
                self.log_text.insert("end", line + "\n")
                self.log_text.see("end")
        except queue.Empty:
            pass
        self.after(75, self._poll_logs)

    def clear_output(self) -> None:
        self.log_text.delete("1.0", "end")
        self.status_var.set("Output cleared.")

    # -------------------------
    # Utilities
    # -------------------------

    def _abs_repo(self) -> Path:
        s = self.repo_root.get().strip() or str(Path.cwd())
        return Path(s).expanduser().resolve()

    def _abs_btg_script(self) -> Path:
        repo = self._abs_repo()
        s = self.btg_script.get().strip()
        if not s:
            guess = guess_btg_script(repo)
            if guess is not None:
                return guess
            return (repo / "tools" / "btg.py").resolve()

        p = Path(s).expanduser()
        return (repo / p).resolve() if not p.is_absolute() else p.resolve()

    def _abs_python_exe(self) -> Path:
        s = self.python_exe.get().strip()
        if not s:
            import sys

            return Path(sys.executable).expanduser().resolve()
        return Path(s).expanduser().resolve()

    def _init_btg_path(self) -> None:
        repo = self._abs_repo()
        guess = guess_btg_script(repo)
        if guess is not None:
            self.btg_script.set(try_rel(repo, guess))
        else:
            self.btg_script.set("")

    def _maybe_update_btg_guess(self) -> None:
        try:
            repo = self._abs_repo()
            current = self._abs_btg_script()
            if not current.exists():
                guess = guess_btg_script(repo)
                if guess is not None:
                    self.btg_script.set(try_rel(repo, guess))
        except Exception:
            pass

    def copy_preview_command(self) -> None:
        cmd = self.cmd_preview.get().strip()
        if not cmd:
            return
        self.master.clipboard_clear()
        self.master.clipboard_append(cmd)
        self.status_var.set("Copied preview command to clipboard.")

    def open_output_folder(self) -> None:
        repo = self._abs_repo()
        out = repo / "output"
        if out.exists():
            open_in_file_manager(out)
            return
        open_in_file_manager(repo)

    def _open_path(self, p: str) -> None:
        try:
            repo = self._abs_repo()
            path = Path(p).expanduser()
            abs_p = (repo / path).resolve() if not path.is_absolute() else path.resolve()
            if abs_p.exists():
                open_in_file_manager(abs_p if abs_p.is_dir() else abs_p.parent)
            else:
                messagebox.showinfo("Not found", f"Path does not exist:\n{abs_p.as_posix()}")
        except Exception as e:
            messagebox.showerror("Open failed", str(e))

    def about(self) -> None:
        messagebox.showinfo(
            "About",
            f"{APP_NAME}\nVersion: {APP_VERSION}\n\n"
            "Tkinter GUI for running btg.py commands with live log output.\n"
            "(Modularized into tools/btg_gui_app/*.py for maintainability.)",
        )

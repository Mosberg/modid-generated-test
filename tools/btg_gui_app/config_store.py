from __future__ import annotations

import json
import os
from pathlib import Path
from tkinter import filedialog, messagebox
from typing import Any, Dict, Optional


REPO_CONFIG_NAME = ".btg_gui.json"
HOME_CONFIG_NAME = ".btg_gui.json"


class ConfigStoreMixin:
    """Persistence for BTG GUI settings.

    Expects the consuming class to define:
      - self.repo_root (tk.StringVar)
      - and all other tk vars used by _collect_config/_apply_config
      - helper self._abs_repo()
      - helper self._maybe_update_btg_guess()
      - helper self._log(msg: str)
      - helper self.status_var (tk.StringVar)

    The implementation is a direct modularization of the earlier monolithic btg_gui.py.
    """

    # -------------------------
    # Config paths
    # -------------------------

    def _config_path_repo(self) -> Path:
        repo = self._abs_repo()
        return repo / REPO_CONFIG_NAME

    def _config_path_home(self) -> Path:
        return Path.home() / HOME_CONFIG_NAME

    def _pick_config_path_for_save(self) -> Path:
        repo_cfg = self._config_path_repo()
        try:
            repo = self._abs_repo()
            if repo.exists():
                if repo_cfg.exists() or os.access(str(repo), os.W_OK):
                    return repo_cfg
        except Exception:
            pass
        return self._config_path_home()

    # -------------------------
    # Load/save
    # -------------------------

    def load_config_best_effort(self) -> None:
        candidates = [self._config_path_repo(), self._config_path_home()]
        for p in candidates:
            try:
                if p.exists():
                    data = json.loads(p.read_text(encoding="utf-8"))
                    if isinstance(data, dict):
                        self._apply_config(data)
                        self._log(f"Loaded config: {p.as_posix()}")
                        self.status_var.set(f"Loaded config: {p.as_posix()}")
                        self._refresh_cmd_preview()
                        return
            except Exception as e:
                self._log(f"Failed to load config {p.as_posix()}: {e}")

        self.status_var.set("No config found; using defaults.")
        self._refresh_cmd_preview()

    def save_config(self) -> None:
        path = self._pick_config_path_for_save()
        try:
            self._write_config(path)
            self._log(f"Saved config: {path.as_posix()}")
            self.status_var.set(f"Saved config: {path.as_posix()}")
        except Exception as e:
            messagebox.showerror("Save Config Failed", str(e))

    def save_config_as(self) -> None:
        repo = self._abs_repo()
        p = filedialog.asksaveasfilename(
            title="Save BTG GUI config",
            initialdir=str(repo),
            initialfile=REPO_CONFIG_NAME,
            defaultextension=".json",
            filetypes=[("JSON", "*.json"), ("All files", "*.*")],
        )
        if not p:
            return
        try:
            self._write_config(Path(p))
            self._log(f"Saved config: {Path(p).as_posix()}")
            self.status_var.set(f"Saved config: {Path(p).as_posix()}")
        except Exception as e:
            messagebox.showerror("Save Config Failed", str(e))

    def _write_config(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        data = self._collect_config()
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    # -------------------------
    # Shape
    # -------------------------

    def _collect_config(self) -> Dict[str, Any]:
        return {
            "app": {"name": "BTG GUI", "version": "2.0.0"},
            "project": {
                "repo_root": self.repo_root.get(),
                "btg_script": self.btg_script.get(),
                "python_exe": self.python_exe.get(),
                "log_level": self.log_level.get(),
                "dry_run": bool(self.global_dry_run.get()),
            },
            "validate": {"schemas": self.val_schemas.get(), "palettes": self.val_palettes.get()},
            "normalize": {"palettes": self.norm_palettes.get()},
            "extract": {
                "textures": self.ext_textures.get(),
                "palettes_out": self.ext_palettes_out.get(),
                "max_colors": self.ext_max_colors.get(),
                "min_alpha": self.ext_min_alpha.get(),
                "schema_ref": self.ext_schema_ref.get(),
                "generator_version": self.ext_generator_version.get(),
            },
            "recolor": {
                "palettes_dir": self.rec_palettes_dir.get(),
                "src_palette": self.rec_src_palette.get(),
                "dst_palette": self.rec_dst_palette.get(),
                "src_id": self.rec_src_id.get(),
                "dst_id": self.rec_dst_id.get(),
                "group": self.rec_group.get(),
                "input": self.rec_input.get(),
                "output": self.rec_output.get(),
                "no_recursive": bool(self.rec_no_recursive.get()),
                "min_alpha": self.rec_min_alpha.get(),
                "alpha_weight": self.rec_alpha_weight.get(),
                "preserve_alpha": bool(self.rec_preserve_alpha.get()),
                "exact_first": bool(self.rec_exact_first.get()),
            },
            "legacy_templates": {
                "palettes_dir": self.leg_palettes_dir.get(),
                "templates_dir": self.leg_templates_dir.get(),
                "output_root": self.leg_output_root.get(),
                "namespace": self.leg_namespace.get(),
                "lang_file": self.leg_lang_file.get(),
                "no_modid_tree": bool(self.leg_no_modid_tree.get()),
                "no_flat_tree": bool(self.leg_no_flat_tree.get()),
            },
            "generate": {
                "templates": self.gen_templates.get(),
                "palettes": self.gen_palettes.get(),
                "output": self.gen_output.get(),
                "min_alpha": self.gen_min_alpha.get(),
                "alpha_weight": self.gen_alpha_weight.get(),
                "preserve_alpha": bool(self.gen_preserve_alpha.get()),
                "exact_first": bool(self.gen_exact_first.get()),
                "limit": self.gen_limit.get(),
            },
            "autotemplate": {
                "templates": self.at_templates.get(),
                "palettes": self.at_palettes.get(),
                "out_dir": self.at_out_dir.get(),
                "materials": self.at_materials.get(),
                "min_alpha": self.at_min_alpha.get(),
                "min_hits": self.at_min_hits.get(),
            },
            "assets": {
                "textures": self.as_textures.get(),
                "recursive": bool(self.as_recursive.get()),
                "items_dir": self.as_items_dir.get(),
                "models_dir": self.as_models_dir.get(),
                "lang": self.as_lang.get(),
                "namespace": self.as_namespace.get(),
                "overwrite_lang": bool(self.as_overwrite_lang.get()),
            },
        }

    def _apply_config(self, data: Dict[str, Any]) -> None:
        proj = data.get("project") or {}
        self.repo_root.set(str(proj.get("repo_root") or self.repo_root.get()))
        self.btg_script.set(str(proj.get("btg_script") or self.btg_script.get()))
        self.python_exe.set(str(proj.get("python_exe") or self.python_exe.get()))
        self.log_level.set(str(proj.get("log_level") or self.log_level.get()))
        self.global_dry_run.set(bool(proj.get("dry_run", self.global_dry_run.get())))

        val = data.get("validate") or {}
        self.val_schemas.set(str(val.get("schemas") or self.val_schemas.get()))
        self.val_palettes.set(str(val.get("palettes") or self.val_palettes.get()))

        norm = data.get("normalize") or {}
        self.norm_palettes.set(str(norm.get("palettes") or self.norm_palettes.get()))

        ext = data.get("extract") or {}
        self.ext_textures.set(str(ext.get("textures") or self.ext_textures.get()))
        self.ext_palettes_out.set(str(ext.get("palettes_out") or self.ext_palettes_out.get()))
        self.ext_max_colors.set(str(ext.get("max_colors") or self.ext_max_colors.get()))
        self.ext_min_alpha.set(str(ext.get("min_alpha") or self.ext_min_alpha.get()))
        self.ext_schema_ref.set(str(ext.get("schema_ref") or self.ext_schema_ref.get()))
        self.ext_generator_version.set(str(ext.get("generator_version") or self.ext_generator_version.get()))

        rec = data.get("recolor") or {}
        self.rec_palettes_dir.set(str(rec.get("palettes_dir") or self.rec_palettes_dir.get()))
        self.rec_src_palette.set(str(rec.get("src_palette") or self.rec_src_palette.get()))
        self.rec_dst_palette.set(str(rec.get("dst_palette") or self.rec_dst_palette.get()))
        self.rec_src_id.set(str(rec.get("src_id") or self.rec_src_id.get()))
        self.rec_dst_id.set(str(rec.get("dst_id") or self.rec_dst_id.get()))
        self.rec_group.set(str(rec.get("group") or self.rec_group.get()))
        self.rec_input.set(str(rec.get("input") or self.rec_input.get()))
        self.rec_output.set(str(rec.get("output") or self.rec_output.get()))
        self.rec_no_recursive.set(bool(rec.get("no_recursive", self.rec_no_recursive.get())))
        self.rec_min_alpha.set(str(rec.get("min_alpha") or self.rec_min_alpha.get()))
        self.rec_alpha_weight.set(str(rec.get("alpha_weight") or self.rec_alpha_weight.get()))
        self.rec_preserve_alpha.set(bool(rec.get("preserve_alpha", self.rec_preserve_alpha.get())))
        self.rec_exact_first.set(bool(rec.get("exact_first", self.rec_exact_first.get())))

        leg = data.get("legacy_templates") or {}
        self.leg_palettes_dir.set(str(leg.get("palettes_dir") or self.leg_palettes_dir.get()))
        self.leg_templates_dir.set(str(leg.get("templates_dir") or self.leg_templates_dir.get()))
        self.leg_output_root.set(str(leg.get("output_root") or self.leg_output_root.get()))
        self.leg_namespace.set(str(leg.get("namespace") or self.leg_namespace.get()))
        self.leg_lang_file.set(str(leg.get("lang_file") or self.leg_lang_file.get()))
        self.leg_no_modid_tree.set(bool(leg.get("no_modid_tree", self.leg_no_modid_tree.get())))
        self.leg_no_flat_tree.set(bool(leg.get("no_flat_tree", self.leg_no_flat_tree.get())))

        gen = data.get("generate") or {}
        self.gen_templates.set(str(gen.get("templates") or self.gen_templates.get()))
        self.gen_palettes.set(str(gen.get("palettes") or self.gen_palettes.get()))
        self.gen_output.set(str(gen.get("output") or self.gen_output.get()))
        self.gen_min_alpha.set(str(gen.get("min_alpha") or self.gen_min_alpha.get()))
        self.gen_alpha_weight.set(str(gen.get("alpha_weight") or self.gen_alpha_weight.get()))
        self.gen_preserve_alpha.set(bool(gen.get("preserve_alpha", self.gen_preserve_alpha.get())))
        self.gen_exact_first.set(bool(gen.get("exact_first", self.gen_exact_first.get())))
        self.gen_limit.set(str(gen.get("limit") or self.gen_limit.get()))

        at = data.get("autotemplate") or {}
        self.at_templates.set(str(at.get("templates") or self.at_templates.get()))
        self.at_palettes.set(str(at.get("palettes") or self.at_palettes.get()))
        self.at_out_dir.set(str(at.get("out_dir") or self.at_out_dir.get()))
        self.at_materials.set(str(at.get("materials") or self.at_materials.get()))
        self.at_min_alpha.set(str(at.get("min_alpha") or self.at_min_alpha.get()))
        self.at_min_hits.set(str(at.get("min_hits") or self.at_min_hits.get()))

        aset = data.get("assets") or {}
        self.as_textures.set(str(aset.get("textures") or self.as_textures.get()))
        self.as_recursive.set(bool(aset.get("recursive", self.as_recursive.get())))
        self.as_items_dir.set(str(aset.get("items_dir") or self.as_items_dir.get()))
        self.as_models_dir.set(str(aset.get("models_dir") or self.as_models_dir.get()))
        self.as_lang.set(str(aset.get("lang") or self.as_lang.get()))
        self.as_namespace.set(str(aset.get("namespace") or self.as_namespace.get()))
        self.as_overwrite_lang.set(bool(aset.get("overwrite_lang", self.as_overwrite_lang.get())))

        self._maybe_update_btg_guess()

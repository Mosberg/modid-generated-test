from __future__ import annotations

from typing import List

from .util import safe_float, safe_int


class BTGCommandMixin:
    """Builds btg.py argv arrays from the GUI variables.

    Expects attributes matching the original monolithic btg_gui.py:
      - self.log_level, self.global_dry_run, ... (tk vars)
    """

    def _global_args(self) -> List[str]:
        out = ["--log", self.log_level.get().strip() or "INFO"]
        if self.global_dry_run.get():
            out.append("--dry-run")
        return out

    def _cmd_validate(self) -> List[str]:
        return [
            "validate",
            "--schemas",
            self.val_schemas.get(),
            "--palettes",
            self.val_palettes.get(),
        ]

    def _cmd_normalize(self) -> List[str]:
        return ["normalize", "--palettes", self.norm_palettes.get()]

    def _cmd_extract(self) -> List[str]:
        max_colors = str(safe_int(self.ext_max_colors.get(), 32))
        min_alpha = str(safe_int(self.ext_min_alpha.get(), 1))
        return [
            "extract",
            "--textures",
            self.ext_textures.get(),
            "--palettes",
            self.ext_palettes_out.get(),
            "--max-colors",
            max_colors,
            "--min-alpha",
            min_alpha,
            "--schema-ref",
            self.ext_schema_ref.get().strip() or "../../schemas/texture-palettes.schema.json",
            "--generator-version",
            self.ext_generator_version.get().strip() or "1.0.0",
        ]

    def _cmd_recolor(self) -> List[str]:
        argv = [
            "recolor",
            "--palettes",
            self.rec_palettes_dir.get(),
            "--src-palette",
            self.rec_src_palette.get(),
            "--dst-palette",
            self.rec_dst_palette.get(),
            "--src-id",
            self.rec_src_id.get(),
            "--dst-id",
            self.rec_dst_id.get(),
            "--input",
            self.rec_input.get(),
            "--output",
            self.rec_output.get(),
            "--min-alpha",
            str(safe_int(self.rec_min_alpha.get(), 1)),
            "--alpha-weight",
            str(safe_float(self.rec_alpha_weight.get(), 0.25)),
        ]

        group = self.rec_group.get().strip()
        if group:
            argv += ["--group", group]
        if self.rec_no_recursive.get():
            argv += ["--no-recursive"]
        if not self.rec_preserve_alpha.get():
            argv += ["--no-preserve-alpha"]
        if not self.rec_exact_first.get():
            argv += ["--no-exact-first"]

        return argv

    def _cmd_legacy_templates(self) -> List[str]:
        argv = [
            "recolor-templates",
            "--palettes",
            self.leg_palettes_dir.get(),
            "--templates",
            self.leg_templates_dir.get(),
            "--output-root",
            self.leg_output_root.get(),
            "--namespace",
            self.leg_namespace.get().strip() or "modid",
            "--lang-file",
            self.leg_lang_file.get().strip() or "en_us.json",
        ]

        if self.leg_no_modid_tree.get():
            argv.append("--no-modid-tree")
        if self.leg_no_flat_tree.get():
            argv.append("--no-flat-tree")
        return argv

    def _cmd_generate(self) -> List[str]:
        argv = [
            "generate",
            "--templates",
            self.gen_templates.get(),
            "--palettes",
            self.gen_palettes.get(),
            "--output",
            self.gen_output.get(),
            "--min-alpha",
            str(safe_int(self.gen_min_alpha.get(), 1)),
            "--alpha-weight",
            str(safe_float(self.gen_alpha_weight.get(), 0.25)),
        ]

        if not self.gen_preserve_alpha.get():
            argv += ["--no-preserve-alpha"]
        if not self.gen_exact_first.get():
            argv += ["--no-exact-first"]

        lim = self.gen_limit.get().strip()
        if lim:
            argv += ["--limit", str(safe_int(lim, 0))]

        return argv

    def _cmd_autotemplate(self) -> List[str]:
        argv = [
            "autotemplate",
            "--templates",
            self.at_templates.get(),
            "--palettes",
            self.at_palettes.get(),
            "--materials",
            self.at_materials.get().strip() or "wood,metal,glass",
            "--min-alpha",
            str(safe_int(self.at_min_alpha.get(), 1)),
            "--min-hits",
            str(safe_int(self.at_min_hits.get(), 2)),
        ]

        out_dir = self.at_out_dir.get().strip()
        if out_dir:
            argv += ["--out-dir", out_dir]
        return argv

    def _cmd_assets(self) -> List[str]:
        argv = [
            "assets",
            "--textures",
            self.as_textures.get(),
            "--items-dir",
            self.as_items_dir.get(),
            "--models-dir",
            self.as_models_dir.get(),
            "--lang",
            self.as_lang.get().strip() or "output/lang/en_us.json",
            "--namespace",
            self.as_namespace.get().strip() or "modid",
        ]

        if self.as_recursive.get():
            argv += ["--recursive"]
        if self.as_overwrite_lang.get():
            argv += ["--overwrite-lang"]
        return argv

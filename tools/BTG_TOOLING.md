# BTG tooling (Python)

This repository now includes a modularized Tkinter GUI wrapper for `btg.py` under `tools/`.  
The GUI is split into several modules for maintainability (config, command building, process runner, utilities).  

## Run

- GUI:
  - `python tools/btg_gui.py`

## Notes

- The GUI expects a `btg.py` script to exist (commonly at `tools/btg.py`).
- If `btg.py` is not present yet, use the GUI's **Browse…** button to select it.
- GUI config is stored as `.btg_gui.json` (prefer repo root if writable, otherwise home directory).

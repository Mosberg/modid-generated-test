#!/usr/bin/env python3

"""BTG GUI entrypoint.

Run:
  python tools/btg_gui.py

This keeps the repo root clean while allowing the GUI to live under tools/.
"""

from btg_gui_app.main import main


if __name__ == "__main__":
    main()

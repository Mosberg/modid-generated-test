from __future__ import annotations

import tkinter as tk

from .gui import BTGGui


def main() -> None:
    root = tk.Tk()
    BTGGui(root)
    root.mainloop()

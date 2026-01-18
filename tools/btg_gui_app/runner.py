from __future__ import annotations

import queue
import subprocess
import threading
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Optional, Sequence

from .util import is_windows, now_ts


@dataclass
class ProcState:
    popen: Optional[subprocess.Popen[str]] = None
    thread: Optional[threading.Thread] = None


class ProcessRunner:
    """Runs a subprocess and streams stdout into a queue."""

    def __init__(
        self,
        log_q: "queue.Queue[str]",
        status_setter: Callable[[str], None],
    ) -> None:
        self._log_q = log_q
        self._status = status_setter
        self._state = ProcState()

    @property
    def running(self) -> bool:
        return self._state.popen is not None

    def log(self, msg: str) -> None:
        try:
            self._log_q.put_nowait(msg)
        except Exception:
            pass

    def start(self, argv: Sequence[str], *, cwd: Path, label: str) -> None:
        if self.running:
            raise RuntimeError("A task is already running")

        creationflags = 0
        if is_windows():
            creationflags = getattr(subprocess, "CREATE_NEW_PROCESS_GROUP", 0)

        def worker() -> None:
            try:
                self._status(f"Running: {label}")
                self._state.popen = subprocess.Popen(
                    list(argv),
                    cwd=str(cwd),
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    universal_newlines=True,
                    creationflags=creationflags,
                )

                assert self._state.popen.stdout is not None
                for line in self._state.popen.stdout:
                    self.log(line.rstrip("\n"))

                rc = self._state.popen.wait()
                self.log(f"[{now_ts()}] INFO: Process exited with code {rc}")
            except Exception as e:
                self.log(f"[{now_ts()}] ERROR: {e}")
            finally:
                self._state.popen = None
                self._status("Ready.")

        self._state.thread = threading.Thread(target=worker, daemon=True)
        self._state.thread.start()

    def stop(self) -> None:
        p = self._state.popen
        if p is None:
            self.log(f"[{now_ts()}] INFO: No process running.")
            return

        self.log(f"[{now_ts()}] INFO: Stop requested.")

        try:
            p.terminate()
        except Exception as e:
            self.log(f"[{now_ts()}] ERROR: terminate failed: {e}")
            return

        def killer() -> None:
            for _ in range(30):
                if self._state.popen is None:
                    return
                if p.poll() is not None:
                    return
                time.sleep(0.1)
            try:
                self.log(f"[{now_ts()}] WARNING: Forcing kill.")
                p.kill()
            except Exception as e:
                self.log(f"[{now_ts()}] ERROR: kill failed: {e}")

        threading.Thread(target=killer, daemon=True).start()

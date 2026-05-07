from __future__ import annotations

import os
import runpy
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PYDEPS = ROOT / "_python_deps"
TOOL_DIR = ROOT / "\u53bb\u6c34\u5370\u5c0f\u5de5\u5177"
APP_FILE = TOOL_DIR / "\u89c6\u9891\u53bb\u6c34\u5370\u52a9\u624b.py"

if PYDEPS.exists():
    sys.path.insert(0, str(PYDEPS))
sys.path.insert(0, str(TOOL_DIR))

if os.environ.get("WATERMARK_TOOL_SELF_TEST") == "1":
    import imageio_ffmpeg
    import watermark_tool_core

    print("launcher ok")
    print(APP_FILE)
    print(watermark_tool_core.__file__)
    print(imageio_ffmpeg.get_ffmpeg_exe())
    raise SystemExit(0)

runpy.run_path(str(APP_FILE), run_name="__main__")

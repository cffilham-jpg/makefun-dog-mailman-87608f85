"""Write one deterministic dog review to the configured output directory.
The missing sausage gives the daily mail delivery one short, dog-minded twist.
"""

import os
from pathlib import Path


LINE = "One star: daily mail, no sausage."

if not LINE.strip():
    raise ValueError("The entry line must not be empty or whitespace-only.")
if len(LINE) > 200:
    raise ValueError("The entry line must be at most 200 characters.")

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_bytes(LINE.encode("utf-8"))

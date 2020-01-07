import sys
from pathlib import Path

parent_path = Path(".").parent
sys.path.insert(0, parent_path)  # noqa: E402

import gimpify  # noqa: F401

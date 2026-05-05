import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.main import app

if __name__ == "__main__":
    dest = sys.argv[1] if len(sys.argv) > 1 else "/dev/stdout"
    with open(dest, "w") as f:
        json.dump(app.openapi(), f, indent=2)

"""Copy the bundled front-page image to the harness output path.

news-image-01 entry for make.fun: the repository ships the finished
illustration as entry.jpg (a 1024 by 1024 JPEG). This script copies those
bytes unchanged to /output/entry.png, so repeated runs produce an identical
file. It needs no network access and uses no clock or randomness.
"""

import hashlib
import sys
from pathlib import Path

REPO_DIR = Path(__file__).resolve().parent
BUNDLED = REPO_DIR / "entry.jpg"
DEST = Path("/output/entry.png")
EXPECTED_SHA256 = "a2bd9d946c94a89fa672f14c8c981a9822924276899b457d85acf65c2255ce7b"


def digest_of(data):
    return hashlib.sha256(data).hexdigest()


def main():
    data = BUNDLED.read_bytes()
    if digest_of(data) != EXPECTED_SHA256:
        sys.exit("bundled image does not match the expected hash")
    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_bytes(data)
    if DEST.stat().st_size != len(data):
        sys.exit("output size does not match the bundled image")
    if digest_of(DEST.read_bytes()) != EXPECTED_SHA256:
        sys.exit("written output does not match the expected hash")


if __name__ == "__main__":
    main()

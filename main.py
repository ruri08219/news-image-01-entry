#!/usr/bin/env python3
"""news-image-01 entry.

Copies the bundled front-page image (entry.jpg) to /output/entry.png
byte-for-byte. The run is fully deterministic: no network access, no
clock reads, no randomness.

Safety: the bundled file is checked against its known SHA-256 and size
before anything is copied, and the written output is re-checked
afterwards. A corrupted or swapped input can never silently produce a
wrong output -- the program exits non-zero instead.
"""

import hashlib
import os
import sys

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.jpg")
DESTINATION = "/output/entry.png"

EXPECTED_SHA256 = "a2bd9d946c94a89fa672f14c8c981a9822924276899b457d85acf65c2255ce7b"
EXPECTED_SIZE = 295051


def sha256_of(path):
    """Return the hex SHA-256 digest of the file at path."""
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def fail(message):
    print(f"error: {message}", file=sys.stderr)
    sys.exit(1)


def main():
    if not os.path.isfile(SOURCE):
        fail(f"bundled image missing: {SOURCE}")

    size = os.path.getsize(SOURCE)
    if size != EXPECTED_SIZE:
        fail(
            f"bundled image has unexpected size: {size} bytes "
            f"(expected {EXPECTED_SIZE})"
        )

    digest = sha256_of(SOURCE)
    if digest != EXPECTED_SHA256:
        fail(
            f"bundled image hash mismatch: got {digest}, "
            f"expected {EXPECTED_SHA256}"
        )

    os.makedirs(os.path.dirname(DESTINATION), exist_ok=True)

    if os.path.exists(DESTINATION) and os.path.samefile(SOURCE, DESTINATION):
        fail("destination resolves to the source file; refusing to "
             "overwrite the bundled image")

    with open(SOURCE, "rb") as src, open(DESTINATION, "wb") as dst:
        for chunk in iter(lambda: src.read(65536), b""):
            dst.write(chunk)

    out_size = os.path.getsize(DESTINATION)
    out_digest = sha256_of(DESTINATION)
    if out_size != EXPECTED_SIZE or out_digest != EXPECTED_SHA256:
        fail(
            f"output verification failed: {DESTINATION} is {out_size} bytes "
            f"with sha256 {out_digest}"
        )

    print(f"wrote {DESTINATION} ({out_size} bytes, sha256 {out_digest})")


if __name__ == "__main__":
    main()

"""news-image-01 entry: write the bundled front-page image to /output/entry.png.

The repository holds the finished image (entry.jpg, 1024x1024 JPEG).
This program only copies those exact bytes to the output path, so every
run produces the same file. No network, no randomness, no clock.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.jpg")
OUTPUT = "/output/entry.png"


def main():
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)
    # Guard: the output must be an exact copy of the bundled image.
    if os.path.getsize(OUTPUT) != os.path.getsize(SOURCE):
        raise RuntimeError("output size does not match the bundled image")


if __name__ == "__main__":
    main()

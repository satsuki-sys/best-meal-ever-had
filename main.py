#!/usr/bin/env python3
"""Write one sentence about the best meal ever had to /output/entry.txt."""

import os

ENTRY = (
    "My grandmother's chicken soup, ladled into a chipped blue bowl "
    "while snow sealed the windows shut, still tastes like winter "
    "deciding, for once, to be kind."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

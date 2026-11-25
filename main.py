#!/usr/bin/env python3
"""Monday, Reviewed in One Line.

Writes the funniest one-line review of my own Monday to /output/entry.txt:
a single line, under 200 characters, no title, no explanation.
"""

import os

LINE = "Monday, one star: my alarm gave up, my inbox hit 47 unread before coffee, and my 9 a.m. meeting should have been an email."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()

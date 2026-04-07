"""
Utilities for working with Clipse's clipboard history
"""

import json
import sys
from pathlib import Path

CLIPSE_DIR = Path.home().joinpath(".config", "clipse")
JSON_FILE = CLIPSE_DIR.joinpath("clipboard_history.json")


def list_entries():
    # print(existing)
    with open(JSON_FILE) as f:
        data = json.load(f)["clipboardHistory"]
        data = sorted(data, key=lambda x: x["recorded"], reverse=True)
        data = sorted(data, key=lambda x: not x["pinned"])

        for datum in data:
            path = datum["filePath"]
            value = datum["value"].replace("\n", " ")
            if path == "null":
                if not value.startswith('<img src="image'):
                    print(datum["recorded"], value)
            else:
                print(datum["recorded"], "img:" + path + ":text:" + value)


def find_recorded(recorded: str):
    with open(JSON_FILE) as f:
        data = json.load(f)["clipboardHistory"]
        for i in data:
            if i["recorded"] == recorded:
                return i


def copy(recorded: str):
    l = recorded.split(" ")
    recorded = " ".join(l[:2])
    data = find_recorded(recorded)
    if data is None:
        return
    if data["filePath"] == "null":
        print(data["value"], end="")
    else:
        sys.stdout.buffer.write(open(data["filePath"], "rb").read())


if sys.argv[1] == "list":
    list_entries()
elif sys.argv[1] == "trim":
    line = sys.argv[2]
    split = line.split(" ", 2)

    if len(split) < 3:
        print(line, end="")
    else:
        print(split[2].strip(), end="")
else:
    copy(sys.stdin.read())

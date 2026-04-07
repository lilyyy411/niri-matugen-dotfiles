"""
Runs matugen in parallel with a partial config file
"""

import os
import subprocess
import sys
import tempfile

NUM_PROCESSES = 4


def run_matugen(entries: list[str], argv: list[str]):
    with tempfile.NamedTemporaryFile("w+") as f:
        # print("Making temp config file", f.name)
        _ = f.write("[config]\nversion_check = false\n" + ("\n".join(entries)))
        # print("Running matugen")
        _ = subprocess.run(["matugen", "-c", f.name, *argv])


def main(argv: list[str]) -> int:
    config_file = argv[1]
    with open(config_file, "r") as f:
        entries = f.read().split("\n\n")
        (*entry_chunks,) = [entries[i::NUM_PROCESSES] for i in range(NUM_PROCESSES)]

        for i in range(NUM_PROCESSES):
            pid = os.fork()
            if pid == 0:
                run_matugen(entry_chunks[i], argv[2:])
                exit(1)
        try:
            while True:
                _ = os.wait()
        except ChildProcessError:
            pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

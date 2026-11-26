"""One Star for Monday — writes the one-star review to /output/entry.txt.

Stdlib only. Reads nothing from the environment except MAKEFUN_OUTPUT_DIR
(the output directory path), no subprocess, no eval, no dynamic import.
"""

import hashlib
import os

ENTRY = (
    "One star. Monday boxed up the leftovers, handed me a doggy bag, "
    "and charged me to take Tuesday home too."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    data = ENTRY.encode("utf-8")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        raise SystemExit("entry.txt mismatch after write")
    print(
        "wrote %d bytes sha256=%s to %s"
        % (len(written), hashlib.sha256(written).hexdigest(), path)
    )


if __name__ == "__main__":
    main()

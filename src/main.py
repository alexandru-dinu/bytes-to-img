#!/usr/bin/env python3

from argparse import ArgumentParser
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def f_truncate(xs: np.ndarray) -> np.ndarray:
    n = np.sqrt(len(xs)).astype(int)
    ys = xs[: n * n].reshape(n, n).astype(np.float32) #/ 255
    return ys


def main():
    xs = {}

    for f in args.files:
        with open(f, "rb") as fp:
            xs[f.stem] = np.frombuffer(fp.read(), dtype=np.uint8)

    a, b = map(f_truncate, xs.values())

    plt.figure(figsize=(10,) * 2)
    sns.heatmap(np.abs(a - b))
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "-f",
        "--files",
        nargs="+",
        type=Path,
        required=True,
        help="Path to the binary file.",
    )
    args = parser.parse_args()

    main()

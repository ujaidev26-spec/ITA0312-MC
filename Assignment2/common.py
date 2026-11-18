"""Shared plotting and reproducibility helpers for Assignment 2."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = Path("figures")
OUT.mkdir(exist_ok=True)

def savefig(name):
    plt.tight_layout()
    path = OUT / name
    plt.savefig(path, dpi=160, bbox_inches="tight")
    plt.close()
    print(f"Saved {path}")

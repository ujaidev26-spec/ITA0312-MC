"""Shared figure output helpers."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
OUT=Path("figures")
OUT.mkdir(exist_ok=True)
def savefig(name):
    plt.tight_layout()
    p=OUT/name
    plt.savefig(p,dpi=160,bbox_inches="tight")
    plt.close()
    print("Saved",p)

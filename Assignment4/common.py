"""Common plotting helper."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
OUT=Path("figures")
OUT.mkdir(exist_ok=True)
def savefig(filename):
    plt.tight_layout()
    path=OUT/filename
    plt.savefig(path,dpi=160,bbox_inches="tight")
    plt.close()
    print("Saved",path)

"""Generate simple explanatory diagrams for Assignment 2."""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from common import OUT

def flow(name,title,labels):
    fig,ax=plt.subplots(figsize=(10,2.3)); ax.set_xlim(0,len(labels)*2); ax.set_ylim(0,2); ax.axis("off")
    xs=[i*2+0.15 for i in range(len(labels))]
    for i,(x,label) in enumerate(zip(xs,labels)):
        box=FancyBboxPatch((x,.65),1.55,.7,boxstyle="round,pad=0.08",fc="#eaf2ff",ec="#315b8a")
        ax.add_patch(box); ax.text(x+.775,1,label,ha="center",va="center",fontsize=9,wrap=True)
        if i<len(labels)-1: ax.add_patch(FancyArrowPatch((x+1.58,1),(xs[i+1]-.05,1),arrowstyle="->",mutation_scale=12))
    ax.set_title(title); fig.savefig(OUT/name,dpi=160,bbox_inches="tight"); plt.close(fig)
    print("Saved",OUT/name)

flow("q1_store_forward_diagram.png","Q1 – Store-and-forward workflow",["Meter sensor","Local storage queue","Check connectivity","Upload reports","Server acknowledgement"])
flow("q2_access_diagram.png","Q2 – Channel access methods",["FDMA: separate frequency bands","TDMA: shared carrier, separate time slots"])
flow("q3_cdma_diagram.png","Q3 – CDMA transmitter and receiver",["User data","Spreading code","Shared noisy channel","Despreading","Detected data"])
flow("q4_ofdma_diagram.png","Q4 – OFDMA subcarrier allocation",["Subcarriers","Scheduler","User 1 / User 2 / …","Parallel data streams"])
flow("q5_sdma_diagram.png","Q5 – SDMA spatial reuse",["Antenna array","Directional beam A","Spatially separated users","Directional beam B"])
flow("q6_decision_diagram.png","Q6 – Technique selection",["Deployment requirements","Rate each technique","Apply criterion weights","Choose highest score"])
flow("q7_redesign_diagram.png","Q7 – Shared telemetry access",["Device report","Random access request","Shared reservation","15 data bursts","Server"])

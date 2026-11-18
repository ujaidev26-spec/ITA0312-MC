"""Q6: DSDV vs AODV comparison using the assignment's reported simulation table."""
import numpy as np
import matplotlib.pyplot as plt
from common import savefig

tests=["20 nodes / 2 m/s","30 nodes / 5 m/s","50 nodes / 10 m/s","50 nodes / 20 m/s","40 nodes / static"]
dsdv_pdr=np.array([77.2,89.2,87.2,76.8,100.0])
aodv_pdr=np.array([77.4,89.6,88.1,81.0,100.0])
dsdv_oh=np.array([7.0,19.3,110.0,212.0,17.8])
aodv_oh=np.array([3.1,3.1,7.5,12.8,0.15])
dsdv_delay=np.array([25,26,24,22,34])
aodv_delay=np.array([31,36,38,46,34])
x=np.arange(len(tests)); w=.36
for name,a,b,ylabel,title,file in [
("PDR",dsdv_pdr,aodv_pdr,"Packet delivery ratio (%)","Q6 – Packet delivery ratio","q6_pdr.png"),
("Overhead",dsdv_oh,aodv_oh,"Control messages per delivered packet","Q6 – Routing control overhead","q6_overhead.png"),
("Delay",dsdv_delay,aodv_delay,"Mean end-to-end delay (ms)","Q6 – Mean end-to-end delay","q6_delay.png")]:
    plt.figure(figsize=(9,4))
    plt.bar(x-w/2,a,w,label="DSDV"); plt.bar(x+w/2,b,w,label="AODV")
    plt.xticks(x,tests,rotation=18,ha="right"); plt.ylabel(ylabel); plt.title(title); plt.legend()
    savefig(file)
for i,t in enumerate(tests):
    print(f"{t}: DSDV PDR={dsdv_pdr[i]:.1f}%, AODV PDR={aodv_pdr[i]:.1f}%, "
          f"overhead={dsdv_oh[i]:.2f}/{aodv_oh[i]:.2f}, delay={dsdv_delay[i]}/{aodv_delay[i]} ms")
print("Decision for a highly dynamic network: AODV; lower control overhead and better PDR at high mobility.")

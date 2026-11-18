"""Q3: Compare cellular and ad hoc network behaviour in a disaster."""
import numpy as np
import matplotlib.pyplot as plt
from common import savefig

labels=["Infrastructure required","Self-healing after node loss","Rapid deployment","Wide-area coverage","Central QoS"]
cellular=np.array([1,0,0,1,1])
adhoc=np.array([0,1,1,0,0])
x=np.arange(len(labels)); w=.36
plt.figure(figsize=(9,4))
plt.bar(x-w/2,cellular,w,label="Cellular")
plt.bar(x+w/2,adhoc,w,label="Ad hoc")
plt.xticks(x,labels,rotation=18,ha="right"); plt.yticks([0,1],["No","Yes"])
plt.ylabel("Capability (qualitative)"); plt.title("Q3 – Cellular vs ad hoc characteristics"); plt.legend()
savefig("q3_architecture_comparison.png")
# Multi-hop capacity approximation: shared single-channel capacity falls roughly as 1/h.
hops=np.arange(1,7); raw_rate=54.0
rate=raw_rate/hops
plt.figure(figsize=(7,4)); plt.plot(hops,rate,marker="o")
plt.xlabel("Number of wireless hops"); plt.ylabel("Approx. per-flow throughput (Mbps)")
plt.title("Q3 – Multi-hop throughput approximation")
savefig("q3_multihop_throughput.png")
for h,r in zip(hops,rate): print(f"{h} hop(s): approximately {r:.1f} Mbps")

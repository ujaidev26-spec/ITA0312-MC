"""Q5: Proactive DSDV routing-table maintenance and sequence numbers."""
import numpy as np
import matplotlib.pyplot as plt
from common import savefig

nodes=["A","B","C","D","E"]
before=[0,1,1,2,3]
after=[0,1,1,2,3] # A-B-D-E remains available after C-D breaks
x=np.arange(len(nodes)); w=.36
plt.figure(figsize=(7,4))
plt.bar(x-w/2,before,w,label="Before C-D failure")
plt.bar(x+w/2,after,w,label="After failure (A-B-D-E route)")
plt.xticks(x,nodes); plt.ylabel("Hop count from node A")
plt.title("Q5 – DSDV route to each destination"); plt.legend()
savefig("q5_dsdv_routes.png")
# Illustrative control-update burden grows with node count and topology change rate.
n=np.array([10,20,30,40,50])
updates=n*n*0.02
plt.figure(figsize=(7,4)); plt.plot(n,updates,marker="o")
plt.xlabel("Number of nodes"); plt.ylabel("Illustrative periodic/triggered update units")
plt.title("Q5 – DSDV control overhead trend (illustrative)")
savefig("q5_dsdv_overhead.png")
print("DSDV rule: higher destination sequence number wins; equal sequence number -> lower hop count wins.")
print("A broken route is advertised with an odd sequence number and infinite metric.")

"""Q7: Hybrid emergency mesh and Mobile IP validation calculations."""
import numpy as np
import matplotlib.pyplot as plt
from common import savefig

# Stage 4A calculations from the assignment scenario.
mn_count=60; rate_kbps=20
ha_load=mn_count*rate_kbps
registration_bytes=160
refresh_seconds=120
print(f"Home Agent traffic load: {ha_load/1000:.2f} Mbps")
print(f"Registration average per MN: {registration_bytes/refresh_seconds:.2f} B/s")
for adv in (1.0,0.5):
    discovery=adv*500
    handoff=50+discovery+20+120+5
    print(f"Advertisement interval {adv:.1f}s -> estimated handoff {handoff:.0f} ms")
loss_fraction=0.7/120*100
print(f"700 ms interruption once per 120 s = {loss_fraction:.2f}% time interruption")
# Stage 4B measured values from assignment table.
tests=["T1: 20 nodes, 2 m/s","T2: 30 nodes, 5 m/s","T3: 50 nodes, 10 m/s","T4: 50 nodes, 20 m/s","T5: 40 nodes, static"]
dsdv=np.array([77.2,89.2,87.2,76.8,100])
aodv=np.array([77.4,89.6,88.1,81.0,100])
x=np.arange(len(tests)); w=.36
plt.figure(figsize=(9,4)); plt.bar(x-w/2,dsdv,w,label="DSDV"); plt.bar(x+w/2,aodv,w,label="AODV")
plt.xticks(x,tests,rotation=18,ha="right"); plt.ylabel("Packet delivery ratio (%)")
plt.title("Q7 – Emergency mesh validation"); plt.legend()
savefig("q7_validation_pdr.png")
# End-to-end delay budget.
parts=["Mesh (3 hops)","LTE / uplink","HA processing"]
low=[30,20,2]; high=[30,60,2]
plt.figure(figsize=(7,4)); plt.bar(parts,[(a+b)/2 for a,b in zip(low,high)],
 yerr=[(b-a)/2 for a,b in zip(low,high)],capsize=5)
plt.ylabel("One-way delay (ms)"); plt.title("Q7 – Emergency message delay budget")
savefig("q7_delay_budget.png")
print("Recommended design: AODV mesh, at least two LTE/5G or satellite gateways, redundant HA,")
print("Mobile IP only for external/control-centre traffic, local AODV for mesh traffic, and 60 s buffering.")

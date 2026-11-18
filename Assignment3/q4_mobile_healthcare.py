"""Q4: Mobile IP application model for ambulance patient monitoring."""
import numpy as np
import matplotlib.pyplot as plt
from common import savefig

components={"Wireless access":(15,30),"Visited network / Internet":(10,10),
            "HA tunnel + processing":(1,2),"Hospital server":(2,2)}
low=sum(v[0] for v in components.values()); high=sum(v[1] for v in components.values())
print("One-way path delay estimate:",low,"to",high,"ms")
names=list(components); mins=[v[0] for v in components.values()]; maxs=[v[1] for v in components.values()]
plt.figure(figsize=(8,4))
plt.bar(names,[(a+b)/2 for a,b in zip(mins,maxs)],yerr=[(b-a)/2 for a,b in zip(mins,maxs)],capsize=5)
plt.xticks(rotation=15,ha="right"); plt.ylabel("Delay (ms)")
plt.title("Q4 – Ambulance monitoring one-way delay budget")
savefig("q4_delay_budget.png")
# Simulate 20-minute journey with handoffs every 4 minutes.
times=np.arange(0,20,0.1)
handoff=np.zeros_like(times)
for t in (4,8,12,16): handoff[(times>=t)&(times<t+0.45)]=1
plt.figure(figsize=(8,3.5)); plt.step(times,1-handoff,where="post")
plt.ylim(-.1,1.1); plt.yticks([0,1],["Handoff interruption","Connected"])
plt.xlabel("Journey time (minutes)"); plt.title("Q4 – Connectivity during ambulance journey")
savefig("q4_ambulance_handoff.png")
print("Scenario: ECG/SpO2 stream 100–500 kbps; target one-way delay <150 ms.")

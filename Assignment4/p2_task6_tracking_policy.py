"""Part II Task 6: simulate an energy-aware tracking/sync policy."""
import matplotlib.pyplot as plt
from common import savefig
minutes=range(0,24*60)
# Example: send updates when moving, batch while stationary; illustrative policy.
events=[]
for m in minutes:
    hour=m//60
    moving=(7<=hour<=9 or 16<=hour<=18)
    if moving and m%5==0: events.append(m)
    elif not moving and m%30==0: events.append(m)
print("Updates in 24 hours:",len(events))
print("Moving window: 5-minute updates; stationary: 30-minute batching.")
plt.figure(figsize=(8,3.5)); plt.scatter(events,[1]*len(events),s=12)
plt.yticks([]); plt.xlabel("Time of day (minutes)"); plt.title("Adaptive tracking update schedule")
savefig("p2_t6_adaptive_schedule.png")

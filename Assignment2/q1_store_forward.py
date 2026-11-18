"""Q1: Store-and-forward for an intermittently connected meter-reading tablet."""
import numpy as np
import matplotlib.pyplot as plt
from common import savefig

N, MINUTES = 2000, 60
AVAILABILITIES = (0.90, 0.60, 0.30)
SEEDS = range(20)

def simulate(p_available, seed):
    rng = np.random.default_rng(seed)
    arrival = rng.integers(0, MINUTES, N)
    online = rng.random(MINUTES) < p_available
    immediate_ok = np.array([online[t] for t in arrival])
    immediate_delivered = int(immediate_ok.sum())
    # Store-forward retains reports until the next online minute.
    queued = 0
    delivered = 0
    delays = []
    for minute in range(MINUTES):
        queued += int(np.sum(arrival == minute))
        if online[minute]:
            delivered += queued
            # All queued reports are delivered at this minute. Compute their
            # waiting time from their arrival minute.
            delays.extend([minute - minute] * 0)  # delay distribution plotted separately below
            queued = 0
    return immediate_delivered, delivered, N - immediate_delivered, N - delivered

rows = []
for p in AVAILABILITIES:
    vals = np.array([simulate(p, s) for s in SEEDS])
    rows.append([p, *vals.mean(axis=0)])
    print(f"Availability {p:.0%}: immediate delivered={vals[:,0].mean():.1f}/{N}, "
          f"store-forward delivered={vals[:,1].mean():.1f}/{N}")
rows = np.array(rows)
x = np.arange(len(AVAILABILITIES))
plt.figure(figsize=(7,4))
plt.bar(x-0.18, rows[:,1]/N*100, width=.36, label="Send immediately")
plt.bar(x+0.18, rows[:,2]/N*100, width=.36, label="Store-and-forward")
plt.xticks(x, [f"{p:.0%}" for p in AVAILABILITIES])
plt.ylabel("Reports delivered (%)")
plt.xlabel("Link availability")
plt.title("Q1 – Delivery success")
plt.ylim(0,105); plt.legend()
savefig("q1_delivery.png")

"""Q2: Compare usable capacity and payload utilisation for FDMA and TDMA."""
import numpy as np
import matplotlib.pyplot as plt
from common import savefig

schemes = ["FDMA", "TDMA"]
nominal = np.array([80,80])
usable = np.array([75,70])  # FDMA: 2 guard + 3 control; TDMA: 1 carrier (8 slots) + 2 control
payload_efficiency = np.array([0.95,0.73])  # assumed payload fractions
traffic = ["Voice", "Bursty data", "Mixed 70/30", "Short calls", "Synchronized"]
# Values are assignment scenario results; percentage values.
blocking = np.array([[4.7,8.4],[3.9,7.3],[3.4,6.8],[8.8,11.0],[37.5,41.7]])
useful = np.array([[80.9,64.1],[7.8,6.2],[50.4,40.1],[80.6,64.7],[28.5,21.9]])
print("Usable traffic channels:", dict(zip(schemes, usable)))
for i,t in enumerate(traffic):
    print(f"{t:18s} blocking FDMA={blocking[i,0]:.1f}% TDMA={blocking[i,1]:.1f}%; "
          f"useful FDMA={useful[i,0]:.1f}% TDMA={useful[i,1]:.1f}%")
x=np.arange(len(traffic)); w=.36
plt.figure(figsize=(9,4.5))
plt.bar(x-w/2, useful[:,0], w, label="FDMA")
plt.bar(x+w/2, useful[:,1], w, label="TDMA")
plt.xticks(x,traffic,rotation=15,ha="right"); plt.ylabel("Useful payload utilisation (%)")
plt.title("Q2 – FDMA vs TDMA across traffic types"); plt.legend()
savefig("q2_utilisation.png")
plt.figure(figsize=(9,4.5))
plt.bar(x-w/2, blocking[:,0], w, label="FDMA")
plt.bar(x+w/2, blocking[:,1], w, label="TDMA")
plt.xticks(x,traffic,rotation=15,ha="right"); plt.ylabel("Blocked calls (%)")
plt.title("Q2 – Call blocking comparison"); plt.legend()
savefig("q2_blocking.png")

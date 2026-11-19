"""Part II Task 5: simple energy accounting model for background policies."""
import matplotlib.pyplot as plt
from common import savefig
# Relative per-hour units: radio wake cost + compute cost; assumptions illustrative.
policies={"Polling every 1 min":60*2.0,"Polling every 15 min":4*2.0,
          "Batched sync":6*1.2,"Push event":3*1.0}
for name,val in policies.items(): print(f"{name}: model energy={val:.1f} units/hour")
plt.figure(figsize=(7,4)); plt.bar(policies.keys(),policies.values())
plt.ylabel("Relative energy units/hour (model)"); plt.xticks(rotation=15,ha="right")
plt.title("Energy model for background tracking strategies")
savefig("p2_t5_energy_model.png")

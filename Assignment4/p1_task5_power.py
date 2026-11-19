"""Part I Task 5: Illustrative power-saving policy effects."""
import matplotlib.pyplot as plt
from common import savefig
policies=["Continuous polling","Frequent sync","Batched sync","Push + batching"]
energy=[100,82,48,35] # relative model units, illustrative
for p,e in zip(policies,energy): print(f"{p}: relative energy index={e}")
plt.figure(figsize=(7,4)); plt.bar(policies,energy)
plt.ylabel("Relative energy units (illustrative)"); plt.xticks(rotation=15,ha="right")
plt.title("Power-control strategy comparison")
savefig("p1_t5_power_policy.png")

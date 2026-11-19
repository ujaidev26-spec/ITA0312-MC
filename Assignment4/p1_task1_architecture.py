"""Part I Task 1: Android architecture layers and responsibility model."""
import matplotlib.pyplot as plt
from common import savefig
layers=["Applications","Application Framework","ART + Core Libraries","Native Libraries","HAL","Linux Kernel","Hardware"]
responsibilities=["App UI / components","System services + SDK APIs","DEX execution + GC","Media, TLS, SQLite, graphics","Vendor device interfaces","Drivers, Binder, scheduling, SELinux","CPU, memory, sensors, modem"]
print("Request path: App SDK -> Binder service -> permission check -> HAL -> kernel driver -> hardware")
for l,r in zip(layers,responsibilities): print(f"{l}: {r}")
plt.figure(figsize=(8,5))
plt.barh(layers,range(len(layers),0,-1))
plt.xlabel("Layer (illustrative ordering only)")
plt.title("Android system architecture layers")
savefig("p1_t1_architecture_layers.png")

"""Part I Task 2: background encrypted messaging model across platforms."""
import matplotlib.pyplot as plt
from common import savefig
platforms=["Android","iOS","Windows"]
services=["FCM","APNs","WNS"]
process_rules=["OS-controlled callback","Notification extension / OS alert","Supported background activation"]
for p,s,r in zip(platforms,services,process_rules): print(f"{p}: push={s}; processing={r}")
stages=["Push service","OS routes","Wake/extension","Fetch + decrypt","Notify","Return idle"]
plt.figure(figsize=(9,3.5)); plt.plot(range(len(stages)),range(len(stages)),marker="o")
plt.xticks(range(len(stages)),stages,rotation=20,ha="right"); plt.yticks([])
plt.title("Encrypted background message delivery sequence")
savefig("p1_t2_message_flow.png")

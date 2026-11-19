"""Part I Task 6: RuralCare cross-platform design recommendation."""
import matplotlib.pyplot as plt
from common import savefig
modules=["UI/business logic","Push notifications","Background jobs","Secure storage","Location/sensors"]
shared=[1,0,0,0,0]
native=[0,1,1,1,1]
x=range(len(modules)); w=.36
plt.figure(figsize=(8,4)); plt.bar([i-w/2 for i in x],shared,w,label="Shared layer"); plt.bar([i+w/2 for i in x],native,w,label="Platform adapters")
plt.xticks(list(x),modules,rotation=20,ha="right"); plt.yticks([0,1],["No","Yes"])
plt.ylabel("Implementation location"); plt.title("Cross-platform app: shared code vs native adapters"); plt.legend()
savefig("p1_t6_crossplatform.png")
print("Recommendation: share UI/business logic where practical; use native adapters for permissions, background work, push, secure storage and sensors.")

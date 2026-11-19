"""Part I Task 4: Security threat-to-mitigation checklist."""
import matplotlib.pyplot as plt
from common import savefig
risks=["Broad permissions","Plain token storage","Unverified update","HTTP transport"]
mitigations=["Ask in context","Keystore-backed key","Verify signer","HTTPS/TLS"]
for r,m in zip(risks,mitigations): print(f"Risk: {r} -> Mitigation: {m}")
plt.figure(figsize=(8,4)); plt.bar(risks,[4,5,4,5])
plt.ylabel("Illustrative severity (1–5)"); plt.ylim(0,5.5)
plt.title("SecureNotes example: risk checklist (qualitative)")
savefig("p1_t4_security_risks.png")

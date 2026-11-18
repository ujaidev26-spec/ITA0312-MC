"""Q4: OFDMA subcarrier allocation comparison."""
import numpy as np
import matplotlib.pyplot as plt
from common import savefig

rng=np.random.default_rng(11)
N_SC, N_USERS=64,8
snr_db=rng.normal(12,5,size=(N_USERS,N_SC))
snr=10**(snr_db/10)
rate=np.log2(1+snr)
def allocate_contiguous():
    a=np.zeros_like(rate)
    for u in range(N_USERS): a[u,u*(N_SC//N_USERS):(u+1)*(N_SC//N_USERS)]=1
    return a
def allocate_interleaved():
    a=np.zeros_like(rate)
    for u in range(N_USERS): a[u,u::N_USERS]=1
    return a
def allocate_best():
    a=np.zeros_like(rate)
    owners=np.argmax(rate,axis=0)
    a[owners,np.arange(N_SC)]=1
    return a
def metrics(a):
    user_rate=(a*rate).sum(axis=1)
    total=user_rate.sum()
    jain=total**2/(N_USERS*np.sum(user_rate**2)) if np.sum(user_rate**2)>0 else 0
    return total,user_rate,jain
schemes={"Contiguous":allocate_contiguous(),"Interleaved":allocate_interleaved(),"Best-channel":allocate_best()}
for name,a in schemes.items():
    total,ur,j=metrics(a)
    print(f"{name}: sum rate={total:.2f} bit/s/Hz, Jain fairness={j:.3f}")
names=list(schemes)
totals=[metrics(schemes[n])[0] for n in names]
fair=[metrics(schemes[n])[2] for n in names]
plt.figure(figsize=(7,4)); plt.bar(names,totals); plt.ylabel("Sum spectral efficiency (bit/s/Hz)")
plt.title("Q4 – OFDMA allocation throughput"); savefig("q4_throughput.png")
plt.figure(figsize=(7,4)); plt.bar(names,fair); plt.ylabel("Jain fairness index"); plt.ylim(0,1.05)
plt.title("Q4 – OFDMA allocation fairness"); savefig("q4_fairness.png")

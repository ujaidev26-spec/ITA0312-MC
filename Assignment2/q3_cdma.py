"""Q3: DS-CDMA spreading, Walsh orthogonality and near-far effect. NumPy only."""
import numpy as np
import matplotlib.pyplot as plt
from common import savefig

EBNO_DB, NBITS = 8.0, 20000

def walsh_codes(L, K):
    if L < 1 or L & (L-1):
        raise ValueError("Code length L must be a positive power of two")
    H=np.array([[1.0]])
    while H.shape[0] < L:
        H=np.block([[H,H],[H,-H]])
    return H[:K]

def ber_trial(codes, amplitudes, ebno_db, seed, asynchronous=False):
    rng=np.random.default_rng(seed)
    K,L=codes.shape
    bits=rng.choice([-1.0,1.0],size=(K,NBITS))
    tx=bits[:,:,None]*codes[:,None,:]*amplitudes[:,None,None]
    if asynchronous and K>1:
        # A one-chip cyclic offset is a simple timing-mismatch model.
        tx[1]=np.roll(tx[1],1,axis=1)
    signal=tx.sum(axis=0)
    ebno=10**(ebno_db/10)
    noise_sigma=np.sqrt(L/(2*ebno))
    rx=signal+rng.normal(0,noise_sigma,size=signal.shape)
    decision=(rx*codes[0]).sum(axis=1)
    return np.mean(np.sign(decision)!=bits[0])

for L in (8,16,64):
    K=max(2,L//4)
    walsh=walsh_codes(L,K)
    random_codes=np.random.default_rng(1000+L).choice([-1.0,1.0],size=(K,L))
    print(f"L={L}, K={K}, Walsh BER={ber_trial(walsh,np.ones(K),EBNO_DB,2000+L):.5f}, "
          f"random BER={ber_trial(random_codes,np.ones(K),EBNO_DB,3000+L):.5f}")
L=64; K=8
codes=walsh_codes(L,K)
cases=["Equal power","Interferer +10 dB","Interferer +20 dB"]
bers=[]
for j,db in enumerate((0,10,20)):
    amps=np.ones(K); amps[1]=10**(db/20)
    bers.append(ber_trial(codes,amps,EBNO_DB,4000+j,asynchronous=True))
plt.figure(figsize=(7,4))
plt.bar(cases,bers); plt.ylabel("BER of desired user"); plt.title("Q3 – Near-far effect (timing offset model)")
plt.xticks(rotation=12,ha="right")
savefig("q3_near_far.png")

"""Q5: SDMA directional reuse with a uniform linear array (idealised model)."""
import numpy as np
import matplotlib.pyplot as plt
from common import savefig

def array_factor(theta_deg, steer_deg, n):
    theta=np.deg2rad(theta_deg); steer=np.deg2rad(steer_deg)
    phase=np.pi*(np.sin(theta)-np.sin(steer))
    weights=np.arange(n)-(n-1)/2
    af=np.exp(1j*phase[:,None]*weights).sum(axis=1)/n
    return np.abs(af)**2
separations=np.arange(5,61,5); sizes=[2,4,8,16]
sir={}
for n in sizes:
    vals=[]
    for sep in separations:
        desired=array_factor(np.array([0.0]),0,n)[0]
        interference=array_factor(np.array([sep]),0,n)[0]
        vals.append(10*np.log10((desired+1e-12)/(interference+1e-12)))
    sir[n]=vals
    print(f"N={n}: SIR at 30 degrees={sir[n][5]:.2f} dB")
plt.figure(figsize=(7,4.5))
for n in sizes: plt.plot(separations,sir[n],marker="o",label=f"{n} elements")
plt.axhline(10,linestyle="--",label="10 dB assumed threshold")
plt.xlabel("Angular separation (degrees)"); plt.ylabel("Idealised SIR (dB)")
plt.title("Q5 – SDMA spatial separation"); plt.legend()
savefig("q5_sir.png")

"""Q7: Compare dedicated TDMA slots with a shared random-access telemetry pool."""
import numpy as np
import matplotlib.pyplot as plt
from common import savefig

DEVICES=300
REPORT_BITS=1600
SLOT_BITS=114
BURSTS_PER_REPORT=int(np.ceil(REPORT_BITS/SLOT_BITS))
MINUTES=5
FRAMES_PER_MINUTE=60/0.004615
TOTAL_FRAMES=int(MINUTES*FRAMES_PER_MINUTE)
USABLE_TDMA_SLOTS=70
CONTENTION_SLOTS=4

def dedicated():
    # A dedicated slot per device is impossible when devices exceed usable slots.
    admitted=min(DEVICES,USABLE_TDMA_SLOTS)
    return admitted, admitted/DEVICES, (DEVICES-admitted)

def shared(seed=300):
    rng=np.random.default_rng(seed)
    # Each device generates one report per minute. Random-access requests
    # contend in a small pool; successful reports reserve 15 bursts.
    pending=[]
    completed=0
    collisions=0
    remaining={}
    for frame in range(TOTAL_FRAMES):
        if frame % int(FRAMES_PER_MINUTE) == 0:
            for d in range(DEVICES):
                pending.append((d,frame))
        # New reservation requests contend in the first four access slots.
        if pending:
            contenders=min(len(pending),CONTENTION_SLOTS)
            chosen=rng.choice(len(pending),size=contenders,replace=False)
            if contenders>1:
                collisions += contenders
            else:
                idx=int(chosen[0]); d,created=pending.pop(idx)
                remaining[d]=BURSTS_PER_REPORT
        finished=[]
        for d in list(remaining):
            remaining[d]-=1
            if remaining[d]<=0:
                completed+=1; finished.append(d)
        for d in finished: del remaining[d]
    return completed,collisions

admitted,fraction,blocked=dedicated()
print(f"Dedicated TDMA: {admitted}/{DEVICES} devices admitted; {blocked} cannot receive a dedicated slot.")
print(f"Each report needs {BURSTS_PER_REPORT} bursts (ceil({REPORT_BITS}/{SLOT_BITS})).")
for seed in (300,301,302):
    delivered,collisions=shared(seed)
    print(f"Shared access seed {seed}: completed reports={delivered}, contention events={collisions}")
plt.figure(figsize=(6.5,4))
plt.bar(["Dedicated slots","Shared access (seed 300)"],[admitted,shared(300)[0]])
plt.ylabel("Reports / devices served in 5 minutes")
plt.title("Q7 – Dedicated versus shared telemetry access")
savefig("q7_access_comparison.png")

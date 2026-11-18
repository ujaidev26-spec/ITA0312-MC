"""Q6: Weighted multiple-access decision matrix.
Ratings and weights below are explicit illustrative judgements, not measured facts.
"""
import numpy as np
import matplotlib.pyplot as plt
from common import savefig

schemes=["SDMA","TDMA","FDMA","CDMA","OFDMA"]
criteria=["Capacity","Interference","Complexity","QoS","Flexibility"]
weights=np.array([.25,.20,.15,.20,.20])
scenarios={
"D1 Cellular voice":np.array([[3,2,2,3,3],[3,3,2,4,5],[4,3,1,5,5],[5,4,3,2,3],[4,3,3,3,3]]),
"D2 Tactical link":np.array([[2,3,1,3,2],[2,1,2,3,4],[2,1,2,4,5],[3,5,2,2,3],[3,2,2,3,3]]),
"D3 Stadium downlink":np.array([[3,2,3,3,2],[3,2,3,3,4],[2,2,2,4,4],[2,3,3,2,3],[5,3,4,3,4]]),
"D4 Sensor network":np.array([[2,2,2,2,2],[1,2,2,3,4],[1,2,1,4,4],[3,4,3,2,3],[3,3,4,3,3]])}
for title,m in scenarios.items():
    scores=m@weights
    winner=schemes[int(np.argmax(scores))]
    print(title, "scores:", dict(zip(schemes,np.round(scores,2))), "winner:",winner)
    plt.figure(figsize=(7,3.8)); plt.bar(schemes,scores)
    plt.ylabel("Weighted score (1–5)"); plt.ylim(0,5.2); plt.title(title)
    savefig("q6_"+title.split()[0].lower()+"_scores.png")

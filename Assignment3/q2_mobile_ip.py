"""Q2: Mobile IP registration, tunnelling overhead and handoff delay."""
import numpy as np
import matplotlib.pyplot as plt
from common import savefig

L2_MS=50
REG_RTT_MS=90
intervals=np.array([0.2,0.5,1.0,1.5])
delay=L2_MS+(intervals*500)+REG_RTT_MS # mean discovery = half advertisement interval
for t,d in zip(intervals,delay):
    print(f"Advertisement interval {t:.1f}s -> handoff delay {d:.0f} ms")
plt.figure(figsize=(7,4)); plt.plot(intervals,delay,marker="o")
plt.axhline(150,linestyle="--",label="150 ms target")
plt.xlabel("Agent advertisement interval (s)"); plt.ylabel("Handoff delay (ms)")
plt.title("Q2 – Mobile IP handoff delay"); plt.legend()
savefig("q2_handoff_delay.png")
payload=np.array([40,100,512,1400])
extra=20
overhead=extra/(payload+20)*100
plt.figure(figsize=(7,4)); plt.bar([str(x) for x in payload],overhead)
plt.xlabel("Application payload (bytes)"); plt.ylabel("Outer tunnel header overhead (%)")
plt.title("Q2 – IP-in-IP tunnelling overhead")
savefig("q2_tunnel_overhead.png")
for p,o in zip(payload,overhead): print(f"Payload={p} B, tunnel overhead={o:.1f}%")
pps=50
for ms in (240,640):
    print(f"At {pps} packets/s and {ms} ms interruption: {pps*ms/1000:.0f} packets may be lost")

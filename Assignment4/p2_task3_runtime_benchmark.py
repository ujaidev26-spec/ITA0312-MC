"""Part II Task 3: compute-heavy vs allocation-heavy runtime benchmark."""
import time
import gc
import matplotlib.pyplot as plt
from common import savefig
def compute(n):
    return sum((i*i)%101 for i in range(n))
def allocate(n):
    a=[bytearray(256) for _ in range(n)]
    return sum(len(x) for x in a)
sizes=[100000,300000,600000]
compute_s=[]; alloc_s=[]
for n in sizes:
    t=time.perf_counter(); compute(n); compute_s.append(time.perf_counter()-t
    )
    gc.collect(); t=time.perf_counter(); allocate(n); alloc_s.append(time.perf_counter()-t)
    print(f"n={n}: compute={compute_s[-1]:.3f}s, allocation={alloc_s[-1]:.3f}s")
plt.figure(figsize=(7,4)); plt.plot(sizes,compute_s,marker="o",label="Compute loop"); plt.plot(sizes,alloc_s,marker="o",label="Allocation workload")
plt.xlabel("Workload size"); plt.ylabel("Elapsed seconds"); plt.title("Runtime benchmark (measured on executing machine)"); plt.legend()
savefig("p2_t3_runtime_benchmark.png")

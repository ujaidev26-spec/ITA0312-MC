"""Part II Task 2: single-thread vs parallel work demonstration (portable Python)."""
import time
from concurrent.futures import ThreadPoolExecutor
import numpy as np
import matplotlib.pyplot as plt
from common import savefig
# CPU-bound Python threads may not speed up due to the GIL; this is an honest benchmark.
N=3000000
def work(start,stop):
    total=0
    for i in range(start,stop): total += (i*i)%97
    return total
def timed_single():
    t=time.perf_counter(); value=work(0,N); return time.perf_counter()-t,value
def timed_threads(k):
    chunks=[(i*N//k,(i+1)*N//k) for i in range(k)]
    t=time.perf_counter()
    with ThreadPoolExecutor(max_workers=k) as ex: vals=list(ex.map(lambda p:work(*p),chunks))
    return time.perf_counter()-t,sum(vals)
single,ref=timed_single(); print("Single worker seconds:",round(single,3))
times=[single]
for k in (2,4,8):
    elapsed,value=timed_threads(k); times.append(elapsed)
    print(f"{k} threads: {elapsed:.3f}s; output matches={value==ref}")
plt.figure(figsize=(7,4)); plt.bar(["1 worker","2 threads","4 threads","8 threads"],times)
plt.ylabel("Elapsed time (s)"); plt.title("Python CPU-bound benchmark (device-specific)")
savefig("p2_t2_thread_benchmark.png")

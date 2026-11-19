"""Part I Task 3: compare runtime approaches and launch types (illustrative)."""
import matplotlib.pyplot as plt
from common import savefig
methods=["Interpreter","JIT","AOT"]
startup=[1.0,0.85,0.65] # relative illustrative startup cost
steady=[1.5,0.8,0.65] # relative compute time; lower is better
print("Illustrative relative values only; not measured platform benchmarks.")
for m,s,c in zip(methods,startup,steady): print(m,": startup index",s,"steady index",c)
x=range(3); w=.36
plt.figure(figsize=(7,4)); plt.bar([i-w/2 for i in x],startup,w,label="Startup cost"); plt.bar([i+w/2 for i in x],steady,w,label="Steady compute cost")
plt.xticks(list(x),methods); plt.ylabel("Relative index (lower is better)"); plt.title("Runtime strategy trade-off (illustrative)"); plt.legend()
savefig("p1_t3_runtime_tradeoff.png")
launch=["Cold","Warm","Hot"]; cost=[3,2,1]
plt.figure(figsize=(6,4)); plt.bar(launch,cost); plt.ylabel("Relative launch work"); plt.title("Cold, warm and hot launch comparison")
savefig("p1_t3_launch_types.png")

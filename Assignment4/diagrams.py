"""Generate conceptual figures for Assignment 4."""
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from common import OUT
def flow(name,title,labels):
 fig,ax=plt.subplots(figsize=(10,2.4)); ax.set_xlim(0,len(labels)*2); ax.set_ylim(0,2); ax.axis("off")
 xs=[i*2+.15 for i in range(len(labels))]
 for i,(x,label) in enumerate(zip(xs,labels)):
  box=FancyBboxPatch((x,.65),1.55,.7,boxstyle="round,pad=.08",fc="#eaf2ff",ec="#315b8a")
  ax.add_patch(box); ax.text(x+.775,1,label,ha="center",va="center",fontsize=9,wrap=True)
  if i<len(labels)-1: ax.add_patch(FancyArrowPatch((x+1.58,1),(xs[i+1]-.05,1),arrowstyle="->",mutation_scale=12))
 ax.set_title(title); fig.savefig(OUT/name,dpi=160,bbox_inches="tight"); plt.close(fig); print("Saved",OUT/name)
flow("p1_t1_request_path.png","Android privileged request path",["Application API","Binder IPC","Permission check","HAL interface","Kernel driver","Hardware"])
flow("p1_t2_push_flow.png","Encrypted push message",["Push service","OS dispatch","App/extension","Fetch + decrypt","Notification"])
flow("p1_t3_cold_launch.png","Cold launch sequence",["Launcher","Activity manager","Zygote process","ART + app init","Activity","First frame"])
flow("p1_t4_secure_sync.png","Secure message sync",["Request permission","Private token","HTTPS/TLS","Verify server","Encrypted data"])
flow("p1_t5_power_control.png","Energy-aware background policy",["Batch work","Push trigger","Short processing","Save state","Return to idle"])
flow("p1_t6_ruralcare.png","RuralCare cross-platform architecture",["Shared UI/logic","Platform adapters","Push/background APIs","Secure storage","Sensors/location"])
flow("p2_t1_lifecycle.png","Lifecycle validation",["Foreground","Background","Memory pressure","Process death","Reopen + restore"])
flow("p2_t2_parallel.png","Parallel benchmark",["Reference result","Split chunks","Workers","Combine results","Verify identical"])
flow("p2_t4_security.png","Security audit",["Review permissions","Check storage","Verify TLS","Check signer","Regression tests"])
flow("p2_t6_tracking.png","Adaptive tracking",["Detect context","Moving: frequent","Stationary: batch","Sync","Sleep"])

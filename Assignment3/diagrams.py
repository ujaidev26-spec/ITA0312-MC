"""Create conceptual architecture and protocol diagrams for Assignment 3."""
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from common import OUT

def draw(name,title,labels):
    fig,ax=plt.subplots(figsize=(10,2.5)); ax.set_xlim(0,len(labels)*2); ax.set_ylim(0,2); ax.axis("off")
    xs=[i*2+.15 for i in range(len(labels))]
    for i,(x,label) in enumerate(zip(xs,labels)):
        p=FancyBboxPatch((x,.65),1.55,.7,boxstyle="round,pad=.08",fc="#eaf2ff",ec="#315b8a")
        ax.add_patch(p); ax.text(x+.775,1,label,ha="center",va="center",fontsize=9,wrap=True)
        if i<len(labels)-1: ax.add_patch(FancyArrowPatch((x+1.58,1),(xs[i+1]-.05,1),arrowstyle="->",mutation_scale=12))
    ax.set_title(title); fig.savefig(OUT/name,dpi=160,bbox_inches="tight"); plt.close(fig); print("Saved",OUT/name)

draw("q1_wireless_architecture.png","Q1 – Wireless network architecture",["Mobile node","Access point / base station","Backhaul network","Gateway / router","Internet / server"])
draw("q2_mobile_ip_registration.png","Q2 – Mobile IP registration and tunnelling",["MN obtains CoA","Registration request","Home Agent updates binding","IP-in-IP tunnel","Foreign network delivers packet"])
draw("q3_cellular_adhoc.png","Q3 – Cellular and ad hoc paths",["Cellular: MN → BS → Core","Ad hoc: Node → Node → Node","Optional gateway to Internet"])
draw("q4_ambulance_architecture.png","Q4 – Ambulance patient-monitoring architecture",["ECG / SpO2 monitor","Ambulance gateway (MN)","4G / 5G / Wi-Fi + CoA","Hospital Home Agent","Doctor / EMR server"])
draw("q5_dsdv_flow.png","Q5 – DSDV proactive routing",["Periodic table update","Compare sequence number","Select freshest route","Forward packet"])
draw("q6_aodv_flow.png","Q6 – AODV reactive routing",["Data needs route","Broadcast RREQ","Destination sends RREP","Forward data","RERR on link failure"])
draw("q7_emergency_mesh.png","Q7 – Hybrid emergency communication",["Responders / vehicles","AODV multi-hop mesh","Redundant LTE / satellite gateways","Mobile IP Home Agent","Command centre"])

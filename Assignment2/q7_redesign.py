"""Q7: Compare dedicated TDMA slots with a shared random-access telemetry pool."""
from collections import deque
import numpy as np
import matplotlib.pyplot as plt
from common import savefig

DEVICES = 300
REPORT_BITS = 1600
SLOT_BITS = 114
BURSTS_PER_REPORT = int(np.ceil(REPORT_BITS / SLOT_BITS))
MINUTES = 5
FRAME_SECONDS = 0.004615
FRAMES_PER_MINUTE = round(60 / FRAME_SECONDS)
TOTAL_FRAMES = MINUTES * FRAMES_PER_MINUTE
USABLE_TDMA_SLOTS = 70
CONTENTION_SLOTS = 4

def dedicated():
    admitted = min(DEVICES, USABLE_TDMA_SLOTS)
    return admitted, DEVICES - admitted

def shared(seed=300):
    """Simplified slotted-ALOHA reservation model with exponential-style backoff."""
    rng = np.random.default_rng(seed)
    pending = deque()
    active = []  # remaining data bursts for reports already admitted
    completed = collisions = generated = 0

    for frame in range(TOTAL_FRAMES):
        # One report per device at the start of each minute.
        if frame % FRAMES_PER_MINUTE == 0:
            for device in range(DEVICES):
                pending.append([device, frame, 0])  # device, ready frame, retry count
                generated += 1

        # Advance active reports: one burst per frame until all 15 are sent.
        active = [left - 1 for left in active]
        completed += sum(left <= 0 for left in active)
        active = [left for left in active if left > 0]

        # At most four reservation minislots are available in each frame.
        ready = []
        waiting = deque()
        while pending:
            item = pending.popleft()
            if item[1] <= frame:
                ready.append(item)
            else:
                waiting.append(item)

        if ready:
            slot_groups = [[] for _ in range(CONTENTION_SLOTS)]
            for item in ready:
                slot_groups[int(rng.integers(CONTENTION_SLOTS))].append(item)

            free_data_slots = max(0, USABLE_TDMA_SLOTS - len(active))
            for group in slot_groups:
                if len(group) == 1 and free_data_slots > 0:
                    active.append(BURSTS_PER_REPORT)
                    free_data_slots -= 1
                elif len(group) == 1:
                    item = group[0]
                    item[1] = frame + int(rng.integers(1, 17))
                    waiting.append(item)
                elif len(group) > 1:
                    collisions += len(group)
                    for item in group:
                        item[2] += 1
                        item[1] = frame + int(rng.integers(1, 17))
                        waiting.append(item)
        pending = waiting

    return completed, collisions, generated

admitted, blocked = dedicated()
print(f"Dedicated TDMA: {admitted}/{DEVICES} devices admitted; {blocked} lack a dedicated slot.")
print(f"One {REPORT_BITS}-bit report requires {BURSTS_PER_REPORT} bursts.")
for seed in (300, 301, 302):
    delivered, collisions, generated = shared(seed)
    print(f"Shared access seed {seed}: {delivered}/{generated} reports completed; "
          f"collision attempts={collisions}; pending at end={generated-delivered}")

shared_delivered = shared(300)[0]
plt.figure(figsize=(7, 4))
plt.bar(["Dedicated slots", "Shared random access"],
        [admitted, shared_delivered], color=["steelblue", "seagreen"])
plt.ylabel("Devices / reports served in five minutes")
plt.title("Q7 – Dedicated versus shared telemetry access")
savefig("q7_access_comparison.png")

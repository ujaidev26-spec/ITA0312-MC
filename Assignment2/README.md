# ITA03 Mobile Computing – Assignment 2 (CO2)

This folder contains seven independent Python simulations and diagram generation for Assignment 2.

## Setup
Use Python 3.10 or newer:
```bash
python -m pip install -r requirements.txt
```
Run commands from this folder:
```bash
python q1_store_forward.py
python q2_fdma_tdma.py
python q3_cdma.py
python q4_ofdma.py
python q5_sdma.py
python q6_decision.py
python q7_redesign.py
python diagrams.py
```

Each program prints key results and saves PNG figures under `figures/`. The simulations are educational models, not standards-compliant radio simulators. Assumptions are labelled in the code. Q3 uses NumPy-only Walsh generation (no SciPy dependency).

## Assignment mapping
- Q1: Mobile communication vs mobile computing; store-and-forward
- Q2: FDMA vs TDMA capacity and traffic
- Q3: CDMA orthogonality, spreading and near-far effect
- Q4: OFDMA subcarrier allocation
- Q5: SDMA directional spatial reuse
- Q6: Weighted multiple-access decision matrix
- Q7: Telemetry access redesign and validation

# ITA03 Mobile Computing – Assignment 3 (CO3)

Seven separate Python programs, graphs and conceptual diagrams for the uploaded Assignment 3.

## Install
```bash
python -m pip install -r requirements.txt
```
Run from this folder:
```bash
python q1_wireless_mobility.py
python q2_mobile_ip.py
python q3_cellular_adhoc.py
python q4_mobile_healthcare.py
python q5_dsdv.py
python q6_dsdv_aodv.py
python q7_emergency_network.py
python diagrams.py
```
Generated PNG files are saved in `figures/`.

## Question mapping
- Q1 wireless architecture, mobility and handoff interruption
- Q2 Mobile IP registration, tunnelling, delay, loss and header overhead
- Q3 cellular versus infrastructure-less ad hoc networks
- Q4 Mobile IP for ambulance / mobile healthcare
- Q5 proactive DSDV routing and sequence-number updates
- Q6 reactive AODV and DSDV/AODV comparison using the assignment's reported test table
- Q7 hybrid emergency mesh design and analytical validation

## Notes
The scripts are simplified educational models. Q6 uses the numeric results printed in the assignment report as input data for plotting; it does not claim to reproduce the original packet-level simulator. Q1, Q2, Q3, Q4, Q5 and Q7 use explicit assumptions stated in the code. NumPy and Matplotlib only are required; SciPy is not needed.

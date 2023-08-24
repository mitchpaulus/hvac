#!/usr/bin/env python3

# Print all combinations of NTU and R, ranging from 0 to 5 for NTU, and 0 to 1 for R
# NTU delta = 0.1
# R delta = 0.1

NTU = 0.1
R = 0.1

while NTU <= 5:
    R = 0.1
    while R < 1:
        # Round each to nearest 10th
        NTU = round(NTU, 1)
        R = round(R, 1)
        print(f"{NTU}\t{R}")
        R += 0.1
    NTU += 0.1

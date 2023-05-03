import os
import numpy as np

alpha_s=np.linspace(0.1,1.0,5)
l1_ratio=np.linspace(0.1,1.0,5)
for p1 in alpha_s:
    for p2 in l1_ratio:
        print(f"logging expriments for alpha:{p1},l1_ratio:{p2}")
        os.system(f"python demo.py -a {p1} -l1 {p2}")
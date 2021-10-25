# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import shutil

for i in range(1,7):
    filename = "figure" + str(i) + ".txt"
    filename_copy = "figure_copy" + str(i) + ".txt"
    shutil.copy2(filename, filename_copy)
    
    f=open(filename_copy).readlines()
    mm = float(f[0])
    for i in [0,0]:
        f.pop(i)
    with open(filename_copy,'w') as F:
        F.writelines(f)
        
    image = np.loadtxt(filename_copy, dtype=int)
    
    colsums = np.sum(image, axis=0)
    
    Y = np.nonzero(colsums)
    pxs = len(Y[0])
    if(pxs != 0):
        res = mm/pxs
        print(filename_copy, " ", res)
    else:
        print(filename_copy, " no image")



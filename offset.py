
import numpy as np
import matplotlib.pyplot as plt
import shutil

def process_file(num):
    filename = "img" + str(num) + ".txt"
    filename_copy = "img" + str(num) + "_copy.txt"
    shutil.copy2(filename, filename_copy)
    
    f=open(filename_copy).readlines()
    for i in [0,0]:
        f.pop(i)
    with open(filename_copy,'w') as F:
        F.writelines(f)
        
def colStart(image):
    colsums = np.sum(image, axis=0)
    Y = np.nonzero(colsums)
    return Y[0][0]

def strStart(image):
    strsums = np.sum(image, axis=1)
    X = np.nonzero(strsums)
    return X[0][0]
    
process_file(1)
process_file(2)
image1 = np.loadtxt("img1_copy.txt", dtype=int)
image2 = np.loadtxt("img2_copy.txt", dtype=int)

diff_y = colStart(image1) - colStart(image2)
diff_x = strStart(image1) - strStart(image2)

res = [diff_y,diff_x]
print("offser img1 to img2 (y,x)", res)


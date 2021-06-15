import os
import time
import shutil
import tempfile
import netCDF4
from netCDF4 import Dataset
import numpy as np
import pandas as pd
with open('./SurfaceEmis.txt') as f:
 lines = f.read().splitlines()
 print(lines)
with open('./kkk') as m:
 minus = m.read().splitlines()
 print(minus)
mask = Dataset('mask_file','r', type='netCDF4')

for i in range(0,len(lines)):
    print('Processing '+lines[i])
    input_file1 = Dataset(lines[i],'r+', type='netCDF4')
    print('Processing '+minus[i])
    input_file2 = Dataset(minus[i],'r', type='netCDF4')

#input_file1 = Dataset('emis_20120702.1.CAplusUS_12km.2013base.ncf','r+', type='netCDF4')
#input_file2 = Dataset('agts_l.RWC_CA.20120702.1.CA_12km.2013base_951.ncf','r', type='netCDF4')
    for j in input_file2.variables:
        if j == "TFLAG":
            pass
        else:
            input_file1.variables[j][:]=(input_file1.variables[j][:]-0.1*input_file2.variables[j][:])*mask.variables['MASK'][:]
    input_file1.close()
    input_file2.close()
    print(i)
    print("DONE")

print("DONE: ")
print(" ")




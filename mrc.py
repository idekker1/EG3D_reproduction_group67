# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 17:26:37 2024

@author: danie
"""

import mrcfile

# Path to your .mrc file
mrc_filename = 'C:/Users/danie/Uni/TUD/q3/deep learning/project/eg3d-main/eg3d-main/eg3d/seed0009.mrc'

# Open the .mrc file
with mrcfile.open(mrc_filename, permissive=True) as mrc:
    # Read the data
    datamrc = mrc.data

#%%
    
print('shape and type',datamrc.type,datamrc.shape)
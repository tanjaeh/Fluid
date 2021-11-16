# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 12:59:59 2021

@author: Tanja
"""
import numpy as np
from mayavi import mlab

print("Hello")

# x, y, z, value = np.random.random((4, 40))
x = 0
y = 0
z = 0
value = 1

mlab.points3d(x, y, z, value)

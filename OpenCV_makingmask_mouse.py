# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 18:53:09 2019

@author: ganze
"""
"""
import cv2
import numpy as np

# original image
image = cv2.imread('2.bmp')

# mask (of course replace corners with yours)
mask = np.zeros(image.shape, dtype=np.uint8)
points = [[(10,10), (300,300), (10,300)]]
roi_corners = np.array(points, dtype=np.int32) #pointsOf the polygon Like [[(10,10), (300,300), (10,300)]]
white = (255, 255, 255)
cv2.fillPoly(mask, roi_corners, white)

# apply the mask
masked_image = cv2.bitwise_and(image, mask)

# display your handywork
cv2.imshow('masked image', masked_image)
cv2.waitKey()
cv2.destroyAllWindows()
"""


import cv2
import numpy as np

from pylab import *
from matplotlib.widgets import LassoSelector

image = cv2.imread('2.bmp')

fig, ax = plt.subplots()
ax.imshow(image, cmap='gray')

def onselect(verts):
    print(verts)

lasso = LassoSelector(ax, onselect)

subplots_adjust(left=0.1, bottom=0.1) 
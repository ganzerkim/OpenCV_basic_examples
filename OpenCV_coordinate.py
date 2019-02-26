# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 21:12:12 2019

@author: ganze
"""

#OpenCV의 좌표계

import numpy as np
import cv2 as cv

width = 640
height = 480
bpp = 3

img = np.zeros((height, width, bpp), np.uint8)

img_h = img.shape[0]
img_w = img.shape[1]
img_bpp = img.shape[2]

print(img_h, img_w, img_bpp)

cv.imshow("drawing", img)

cv.waitKey(0)
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 22:09:09 2019

@author: ganze
"""

#선분 그리기

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

red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)
white = (255, 255, 255)
yellow = (0, 255, 255)
cyan = (255, 255, 0)
magenta = (255, 0, 255)


thickness = 10
#오른쪽으로 갈수록 x증가 아래로 갈수록 y증가
cv.line(img, (0, 0), (0, img_h - 1), white, thickness)
cv.line(img, (0, 0), (img_w - 1, 0), blue, thickness)
cv.line(img, (img_w - 1, img_h - 1), (0, img_h - 1), green, thickness)
cv.line(img, (img_w - 1, img_h - 1), (img_w - 1, 0), yellow, thickness)


thickness = 1

cv.line(img, (img_w - 1, 0), (0, img_h - 1), red, thickness)
cv.line(img, (0, 0), (width - 1, img_h - 1), cyan, thickness)

cv.imshow("drawing", img)
cv.waitKey(0)
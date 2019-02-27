# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 21:46:47 2019

@author: ganze
"""

#글자 그리기 

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



thickness = 2 

org = ((int)(img_w / 2) - 200, (int)(img_h / 2) - 100)
font = cv.FONT_HERSHEY_SCRIPT_SIMPLEX  # hand-writing style font
fontScale = 3.5
cv.putText(img, 'OpenCV', org, font, fontScale, yellow, thickness, cv.LINE_AA)


org = ((int)(img_w / 2) - 150, (int)(img_h / 2) + 20)
font = cv.FONT_ITALIC  # italic font
fontScale = 2
cv.putText(img, 'Tutorial', org, font, fontScale, red, thickness, cv.LINE_AA)


org = ((int)(img_w / 2) - 250, (int)(img_h / 2) + 100)
font = cv.FONT_HERSHEY_SIMPLEX  # normal size sans-serif font
fontScale = 1.5
cv.putText(img, 'ganzerkim@gmail.com', org, font, fontScale, blue, thickness, cv.LINE_AA)


org = ((int)(img_w / 2) - 130, (int)(img_h / 2) + 150)
ont = cv.FONT_HERSHEY_COMPLEX  # normal size serif font
fontScale = 1.2
cv.putText(img, 'mingeonkim', org, font, fontScale, green, thickness, cv.LINE_AA)



cv.imshow("drawing", img)
cv.waitKey(0);
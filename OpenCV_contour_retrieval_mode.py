# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 23:47:30 2019

@author: ganze
"""

import cv2 as cv
import numpy as np


img_color = cv.imread('y.png')
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
ret, img_binary = cv.threshold(img_gray, 127, 255, 0)

#contour Retrieval Mode는 총 4가지
#RETR_TREE, RETR_LIST, RETR_EXTERNAL, RETR_CCOMP
#[Next, Previous, First_Child, Parent]
contours, hierarchy = cv.findContours(img_binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)


for cnt in contours:
    cv.drawContours(img_color, [cnt], 0, (255, 0, 0), 3)  # blue

cv.imshow("result", img_color)

cv.waitKey(0)



# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 20:52:47 2019

@author: ganze
"""

#ROI 사용법

import cv2 as cv
import random
import numpy as np

mouse_is_pressing = False
start_x, start_y = -1, -1


def mouse_callback(event,x,y,flags,param):
    global start_x, start_y,mouse_is_pressing

    if event == cv.EVENT_LBUTTONDOWN:

        mouse_is_pressing = True
        start_x, start_y = x, y


    elif event == cv.EVENT_LBUTTONUP:

        mouse_is_pressing = False
        # 원본 영역에서 두 점 (start_y, start_x), (x,y)로 구성되는 사각영역을 잘라내어 변수 img_cat이 참조하도록 합니다. 
        img_supine = img_color[ start_y:y, start_x:x]
        cv.imshow("img_supine", img_supine)

img_color = cv.imread('2.bmp', cv.IMREAD_COLOR )

cv.imshow("img_color", img_color)
cv.setMouseCallback('img_color', mouse_callback)

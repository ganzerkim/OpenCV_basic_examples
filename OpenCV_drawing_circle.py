# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 21:22:26 2019

@author: ganze
"""

#원 그리기 예제

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

def tuple_add(x, y):
    return tuple(np.add(x, y))

red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)
white = (255, 255, 255)
yellow = (0, 255, 255)
cyan = (255, 255, 0)
magenta = (255, 0, 255)


radius = 10
#오른쪽으로 갈수록 x증가 아래로 갈수록 y증가
#img = 원이 그려질 이미지, center = 원의 중심좌표, radius = 원의 반지름, color = 원의 색, 굵기


#thickness = -1 이면 원이 채워지고 1이면 두께
#좌표 0,0 중심에서 원그리면 잘리기 때문에 튜플 10,10을 더해서 좌표를 10, 10으로 변경
thickness = -1
cv.circle(img, tuple_add((0, 0), (10, 10)), radius, red, thickness)

thickness = 1
cv.circle(img, tuple_add((0, img_h - 1), (10, -10)), radius, green, thickness)

thickness = -1
cv.circle(img, tuple_add((img_w - 1, 0), (-10, 10)), radius, blue, thickness)
cv.circle(img, tuple_add((img_w - 1, img_h - 1), (-10, -10)), radius, white, thickness)

cv.imshow("drawing", img)

cv.waitKey(0)
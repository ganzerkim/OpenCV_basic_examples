# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 23:21:47 2019

@author: ganze
"""
# 컨투어

import cv2 as cv


img_color = cv.imread('x.png')
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
ret, img_binary = cv.threshold(img_gray, 127, 255, 0)

#이미지는 검은색과 흰색 즉 바이너리 이미지가 들어가야됨.
#이진화 또는 캐니 적용 필수

img, contours, hierarchy = cv.findContours(img_binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)


for cnt in contours:
    cv.drawContours(img_color, [cnt], 0, (255, 0, 0), 3)  # blue
    #cv.drawContours(img_color, [cnt], 1, (0, 0, 255), 3)
    
    
cv.imshow("result", img_color)

cv.waitKey(0)



for cnt in contours:

    area = cv.contourArea(cnt)

    print(area)


cv.imshow("result", img_color)

cv.waitKey(0)
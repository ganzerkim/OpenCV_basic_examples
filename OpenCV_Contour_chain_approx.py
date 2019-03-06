# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 23:48:21 2019

@author: ganze
"""

import cv2 as cv


img_color = cv.imread('x.png')
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
ret, img_binary = cv.threshold(img_gray, 127, 255, 0)

#이미지는 검은색과 흰색 즉 바이너리 이미지가 들어가야됨.
#이진화 또는 캐니 적용 필수
#Chain_approx_none은 컨투어를 따라 선 전체의 좌표를 저장
#Simple은 선과 선이 잇는 지점 좌표만 저장 메모리 아낄수 있음.
#img, contours, hierarchy = cv.findContours(img_binary, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
img, contours, hierarchy = cv.findContours(img_binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    for p in cnt:
        cv.circle(img_color, (p[0][0], p[0][1]), 10, (255, 0, 0), -1)
    
    
cv.imshow("result", img_color)

cv.waitKey(0)


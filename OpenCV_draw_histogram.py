# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 23:42:03 2019

@author: ganze
"""

#히스토그램 구하기

import cv2 as cv
import numpy as np


bins = np.arange(256).reshape(256,1)


def draw_histogram(img):

    h = np.zeros((img.shape[0], 256), dtype=np.uint8)
#images => uint8 또는 float32 타입의 이미지를 사용해야 하며  대괄호 [ ] 안에 입력해야 합니다. 예) [img]
#channels => 히스토그램을 계산할 채널의 인덱스입니다. 대괄호 [ ] 안에 입력해야 합니다. 
    #예를 들어 그레이스케일 이미지라면 [0] 입니다.  컬러 이미지라면 [0], [1], [2] 중 하나를 사용할 수 있습니다. 각각 파란색, 녹색, 빨간색 채널을 의미합니다.
#mask =>    마스크 이미지. 전체 이미지에대한 히스토그램을 구할 거라면 None을 사용해야 합니다.  이미지 일부분에 대한 히스토그램을 구하려고 한다면 마스크 이미지를 생성하여 제공해야 합니다.
#histSize => 계산할 히스토그램 막대(BIN)의 개수입니다. 대괄호 [ ]안에 입력해야 합니다.  전체 영역을 계산한다면 [256]입니다. 
#ranges => 히스토그램을 계산할 범위입니다. 전체 픽셀 강도 범위를 계산 한다면 [0, 256] 입니다.

    hist_item = cv.calcHist([img],[0],None,[256],[0,256])
    cv.normalize(hist_item,hist_item,0,255,cv.NORM_MINMAX)
    hist=np.int32(np.around(hist_item))
    for x,y in enumerate(hist):
        cv.line(h,(x,0+10),(x,y+10),(255,255,255))

    cv.line(h, (0, 0 + 10), (0, 5), (255, 255, 255) )
    cv.line(h, (255, 0 + 10), (255, 5), (255, 255, 255))
    y = np.flipud(h)

    return y


img = cv.imread('cat.png', cv.IMREAD_COLOR)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


line =  draw_histogram(gray)
result1 = np.hstack((gray, line))
cv.imshow('result1', result1)


cv.waitKey(0)
cv.destroyAllWindows()
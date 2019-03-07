# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 00:10:01 2019

@author: ganze
"""

#CLAHE (contrast limited adapitve histogram equalization)
#이미지를 작은 블럭으로 나눕니다. OpenCV에서 사용하는 디폴트 블럭의 크기는 8x8 입니다. 그리고나서 히스토그램 평활화를 적용합니다. 그 결과 히스토그램이 작은 영역에 한정될 것입니다. 
#노이즈가 있다면 증폭되는데 이것을 방지하기 위해서  콘트라스트를 제한적으로 적용합니다. 
#히스토그램의 특정 막대(bin)가 미리 정한 콘트라스트 값보다 크다면(OpenCV에서는 디폴트로 40) 히스토그램 평활화를 적용하기 전에 해당 막대은 다른 히스토그램 막대에 균일하게 분배합니다. 
#히스토그램 평활화를 적용한 후에 블럭으로 나누었던 것의 효과를 줄이기 위해서 Bilinear Interpolation 보간법을 적용합니다. 

import cv2 as cv
import numpy as np


bins = np.arange(256).reshape(256,1)


def draw_histogram(img):

    h = np.zeros((img.shape[0], 513), dtype=np.uint8)

    hist_item = cv.calcHist([img],[0],None,[256],[0,256])
    cv.normalize(hist_item,hist_item,0,255,cv.NORM_MINMAX)
    hist=np.int32(np.around(hist_item))
    for x,y in enumerate(hist):
        cv.line(h,(x,0+10),(x,y+10),(255,255,255))

    cv.line(h, (0, 0 + 10), (0, 5), (255, 255, 255) )
    cv.line(h, (255, 0 + 10), (255, 5), (255, 255, 255))
    y = np.flipud(h)

    #draw curve
    hist, bin = np.histogram(img.flatten(), 256, [0, 256])
    cdf = hist.cumsum()
    cdf_normalized = cdf * float(hist.max()) / cdf.max()
    cv.normalize(cdf_normalized, cdf_normalized, 0, 255, cv.NORM_MINMAX)
    hist = np.int32(np.around(cdf_normalized))
    pts = np.int32(np.column_stack((bins, hist)))
    pts += [257, 10]

    cv.line(h, (0+257, 0 + 10), (0+257, 5), (255, 255, 255) )
    cv.line(h, (255+257, 0 + 10), (255+257, 5), (255, 255, 255))
    cv.polylines(h, [pts], False, (255,255,255))

    return y


img = cv.imread('face.png', cv.IMREAD_COLOR)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


line =  draw_histogram(gray)
result1 = np.hstack((gray, line))
cv.imshow('result1', result1)


clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
equ = clahe.apply(gray)


line =  draw_histogram(equ)
result2 = np.hstack((equ, line))
cv.imshow('result2', result2)


cv.waitKey(0)
cv.destroyAllWindows()

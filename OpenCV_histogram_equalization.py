# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 23:54:06 2019

@author: ganze
"""

#히스토그램 평활화(histogram equalization)

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


img = cv.imread('cat.png', cv.IMREAD_COLOR)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


line =  draw_histogram(gray)
result1 = np.hstack((gray, line))
cv.imshow('result1', result1)


#equ = cv.equalizeHist(gray)

#이미지를 1차원 배열로 변환 후 히스토그램을 구합니다. 
hist, bin = np.histogram(img.flatten(), 256, [0, 256])
#히스토그램의 누적합을 구합니다. 
cdf = hist.cumsum()
# cdf의 값이 0인 경우는 mask처리를 하여 계산에서 제외시킴
cdf_mask = np.ma.masked_equal(cdf,0)
#누적합의 최대값, 최소값을 이용하여 히스토그램이 넓게 분포되도록 만들어해주는 룩업 테이블( look-up table)을 만듭니다. 
cdf_mask = (cdf_mask - cdf_mask.min())*255/(cdf_mask.max()-cdf_mask.min())
 # Mask처리를 했던 부분을 다시 0으로 변환
cdf = np.ma.filled(cdf_mask,0).astype('uint8')
#룩업 테이블을 그레이스케일 이미지에 적용하여 히스토그램 평활화가 적용된 이미지를 얻습니다. 
equ = cdf[gray]


line =  draw_histogram(equ)
result2 = np.hstack((equ, line))
cv.imshow('result2', result2)


cv.waitKey(0)
cv.destroyAllWindows()
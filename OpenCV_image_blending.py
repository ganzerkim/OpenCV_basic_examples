# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 21:14:04 2019

@author: ganze
"""
# image blending

import cv2 as cv


a = 0.0

while(a <= 1.0):

    img1 = cv.imread('lena.jpg')
    img2 = cv.imread('billard.png')


    # 블렌딩하는 두 이미지의 크기가 같아야함
    width = img1.shape[1]
    height = img1.shape[0]
    img2 = cv.resize(img2, (width, height))

    # img1 사진은 점점 투명해지고 img2 사진은 점점 불투명해짐
    b = 1.0 - a
    dst = cv.addWeighted(img1, a, img2, b, 0)
    cv.imshow('dst',dst)
    cv.waitKey(0)

    print( a, " ", b)

    a = a + 0.2


cv.destroyAllWindows()
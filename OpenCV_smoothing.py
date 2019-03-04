# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:17:13 2019

@author: ganze
"""

#컨볼루션

import numpy as np
import cv2


img = cv2.imread('filter2d_test.png')
kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img, -1, kernel)


cv2.imshow('Original', img)
cv2.imshow('Result', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

#############################################################


#평균 블러링(Averaging Blurring)
#위에처럼 커널을 만들어서 컨볼루션하는 번거로움을 막기 위해 블러링함수제공


import cv2

img = cv2.imread('filter2d_test.png')
blur = cv2.blur(img,(5,5))


cv2.imshow('Original', img)
cv2.imshow('Result', blur)

cv2.waitKey(0)
cv2.destroyAllWindows()

##############################################################


#가우시안 블러링 (Gaussian Blurring)
#평균 블러링은 전체적으로 블러가 되지만 가우시안 블러링은 엣지부분은 최대한
#남기고 블러링이 이루어짐, 캐니(Canny)로 에지를 검출하기전에 노이즈를 제거하기 위해 사용됨.

import cv2


img = cv2.imread('filter2d_test.png')
blur = cv2.GaussianBlur(img,(5,5),0)


cv2.imshow('Original', img)
cv2.imshow('Result', blur)

cv2.waitKey(0)
cv2.destroyAllWindows()

##############################################################

#미디안 블러링(Median Blurring)

#관심화소 주변으로 지정한 커널 크기( 5 x 5) 내의 픽셀을 크기순으로 정렬한 후 중간값을 뽑아서 픽셀값으로 사용합니다.
#무작위 노이즈를 제거하는데 효과적입니다. 하지만 에지가 있는 이미지의 경우에는 결과 이미지에서 에지가 사라질 수 있습니다.



import cv2


img = cv2.imread('noise_circle.png')
median = cv2.medianBlur(img, 5)

cv2.imshow('Original', img)
cv2.imshow('Result', median)

cv2.waitKey(0)
cv2.destroyAllWindows()

############################################################

#bilateral filtering

#에지를 보존하면서 노이즈를 감소시킬수 있는 방법입니다.
#결과 이미지에서 질감있는 부분만 블러링 되고 에지 부분은 보존되었습니다.

import cv2


img = cv2.imread('texture.png')
blur = cv2.bilateralFilter(img,9,75,75)

cv2.imshow('Original', img)
cv2.imshow('Result', blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
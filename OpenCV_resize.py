# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 21:36:31 2019

@author: ganze
"""

import cv2


# 원본 이미지
img_source = cv2.imread('test_resize.bmp')
cv2.imshow("original", img_source)

cv2.waitKey(0)


# 2배 이미지
img_result = cv2.resize(img_source, None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
cv2.imshow("x2", img_result)

cv2.waitKey(0)


# 4배 이미지
height, width = img_source.shape[:2]
img_result = cv2.resize(img_source, (4*width, 4*height), interpolation = cv2.INTER_LINEAR )
cv2.imshow("x4 INTER_LINEAR", img_result)

height, width = img_source.shape[:2]
img_result2 = cv2.resize(img_source, (4*width, 4*height), interpolation = cv2.INTER_CUBIC )
cv2.imshow("x4 INTER_CUBIC", img_result)

cv2.waitKey(0)


# INTER_CUBIC를 사용해 확대한 4배 이미지를 0.5배한 이미지
img_result = cv2.resize(img_result2, None, fx=0.5, fy=0.5, interpolation = cv2.INTER_AREA)
cv2.imshow("x0.5 INTER_AREA", img_result)

img_result = cv2.resize(img_result2, None, fx=0.5, fy=0.5) # cv2.INTER_LINEAR
cv2.imshow("x0.5 INTER_LINEAR", img_result)

cv2.waitKey(0)


cv2.destroyAllWindows()
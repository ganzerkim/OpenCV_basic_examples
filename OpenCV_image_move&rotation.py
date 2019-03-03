# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 21:24:09 2019

@author: ganze
"""
#이미지 이동 및 회전
import numpy as np
import cv2


# 원본 이미지
img_source = cv2.imread('lena.jpg')
cv2.imshow("original", img_source)

cv2.waitKey(0)


# 이미지 이동


height, weight = img_source.shape[:2]
#[[x, 0, tx], [0, y, ty]]
M = np.float32([[1, 0, 100], [0, 1, 25]]) # 이미지를 오른쪽으로 100, 아래로 25 이동시킵니다.
img_translation = cv2.warpAffine(img_source, M, (weight,height))
cv2.imshow("translation", img_translation)

cv2.waitKey(0)


# 이미지 회전
M = cv2.getRotationMatrix2D(((weight-1)/2.0, (weight-1)/2.0), #회전 중심
                            45, # 회전각도(양수 반시계방향, 음수 시계방향)
                            1) # 이미지 배율
img_rotation = cv2.warpAffine(img_source, M, (weight,weight))
cv2.imshow("rotation", img_rotation)

cv2.waitKey(0)


cv2.destroyAllWindows()
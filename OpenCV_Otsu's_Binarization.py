# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:10:20 2019

@author: ganze
"""

#Otsu's Binarization

#THRESH_OTSU와 함께 threshold함수를 사용한 이진화합니다.  이미지에 대한 히스토그램에서 임계값을 자동으로 계산해줍니다. 


import cv2


img_source = cv2.imread('test10.png', 0)

ret,img_result1 = cv2.threshold(img_source, 127, 255, cv2.THRESH_BINARY)

ret, img_result2 = cv2.threshold(img_source, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

img_blur = cv2.GaussianBlur(img_source, (5,5), 0)
ret, img_result3 = cv2.threshold(img_blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)



cv2.imshow("SOURCE", img_source)
cv2.imshow("THRESH_BINARY", img_result1)
cv2.imshow("THRESH_OTSU", img_result2)
cv2.imshow("THRESH_OTSU + Gaussian filtering", img_result3)

cv2.waitKey(0)
cv2.destroyAllWindows()
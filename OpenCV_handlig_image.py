# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 22:01:14 2019

@author: ganze
"""
#이미지 다루기


import cv2

#이미지 불러오기
#이미지 불러올때 사용하는 flag
#retval = cv2.imread(filename, [flags])
#flag ==> cv2.IMREAD_COLOR, cv2.GRAYSCALE, cv2.UNCHANGED(투명도 정보를 포함한 알파채널 포함하여 출력)
img_color = cv2.imread('lena.jpg', cv2.IMREAD_COLOR)

cv2.namedWindow('Show Image')
cv2.imshow('Show Image', img_color)

#키보드 입력이 있을때까지 화면을 띄어놓음
cv2.waitKey(0)

img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

# 동시에 이미지를 보려면 Show Image이름을 다르게 설정하면 된다.
cv2.imshow('Show Image', img_gray)
cv2.waitKey(0)



cv2.imwrite('savedimage.jpg', img_gray)

cv2.destroyAllWindows()
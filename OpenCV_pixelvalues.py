# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 19:09:41 2019

@author: ganze
"""
#픽셀 접근으로 이미지 다루기
"""
import cv2 as cv

img = cv.imread('test.png')

# (y, x) = (50, 50) 좌표의 픽셀값을 읽어오면 [153  43  36]입니다. 좌표 순서가 y, x 순인 것에 유의하세요. 
# 픽셀값은 [blue, green, red] 값으로 구성되어 있는데 blue가 가장 크기 때문에 이미지에서 파란색으로 보입니다.

print(img[50, 50]) 

# 흰색으로 변경하면 아래 결과 영상처럼 파란색 사각형의 왼쪽 아래에 흰점이 출력됩니다.  

img[50, 50] = [255, 255, 255]
print(img[50, 50])

cv.imshow('win', img)

cv.waitKey(0)
"""

"""
import cv2 as cv


img = cv.imread('test.png')


# blue, green, red 순으로 개별적으로 픽셀값을 가져오고 있습니다. 
# 좌표는 (y,x)=(50,50)입니다. 
print(img.item(50,50,0), img.item(50,50,1), img.item(50,50,2))


# blue, green, red 순으로 개별적으로 픽셀값을 255로 설정하고 있습니다.  
img.itemset(50,50, 0, 255) 
img.itemset(50,50, 1, 255)
img.itemset(50,50, 2, 255)

print(img.item(50,50,0), img.item(50,50,1), img.item(50,50,2))


cv.imshow('win', img)

cv.waitKey(0)
"""
"""
#픽셀 접근으로 수직선과 수평선 그리는 법
import numpy as np
import cv2 as cv


img = cv.imread('test.png')

height = img.shape[0]
width = img.shape[1]

for y in range(0,height):
    img.itemset(y,50, 0, 0) 
    img.itemset(y,50, 1, 0) 
    img.itemset(y,50, 2, 0) 

for x in range(0,width):
    img.itemset(50, x, 0, 255) 
    img.itemset(50, x, 1, 255) 
    img.itemset(50, x, 2, 255) 

cv.imshow('win', img)


cv.waitKey(0)
"""

#컬러영상 픽셀접근으로 그레이영상으로 변환하기
import cv2 as cv
import numpy as np


# 카메라에 접근하기 위해 VideoCapture 객체를 생성
cap = cv.VideoCapture(0)


while(True):

    # 이미지를 캡쳐
    ret, img_color = cap.read()

    # 캡쳐되지 않은 경우 처리
    if ret == False:
        continue;

    # 그레이스케일 이미지로 변환
    #img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
    height, width, channel = img_color.shape
    img_gray = np.zeros((height, width), np.uint8)


    for y in range(0, height):
        for x in range(0, width):
            b = img_color.item(y, x, 0)
            g = img_color.item(y, x, 1)
            r = img_color.item(y, x, 2)

            gray = (int(b) + int(g) + int(r)) / 3.0

            if gray > 255:
                gray = 255

            img_gray.itemset(y, x, gray)


    cv.imshow('bgr', img_color)
    # 그레이스케일 이미지를 출력
    cv.imshow('gray', img_gray)

    # ESC 키누르면 종료
    if cv.waitKey(1) & 0xFF == 27:
        break


# VideoCapture 객체를 메모리 해제하고 모든 윈도우 창을 종료합니다.
cap.release()
cv.destroyAllWindows()
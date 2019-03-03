# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 22:33:56 2019

@author: ganze
"""

import numpy as np
import cv2


point_list = []
count = 0

def mouse_callback(event, x, y, flags, param):
    global point_list, count, img_original


    # 마우스 왼쪽 버튼 누를 때마다 좌표를 리스트에 저장
    if event == cv2.EVENT_LBUTTONDOWN:
        print("(%d, %d)" % (x, y))
        point_list.append((x, y))

        print(point_list)
        cv2.circle(img_original, (x, y), 3, (0, 0, 255), -1)



cv2.namedWindow('original')
cv2.setMouseCallback('original', mouse_callback)

# 원본 이미지
img_original = cv2.imread('test2.png')


while(True):

    cv2.imshow("original", img_original)


    height, weight = img_original.shape[:2]


    if cv2.waitKey(1)&0xFF == 32: # spacebar를 누르면 루프에서 빠져나옵니다.
        break



pts1 = np.float32([list(point_list[0]),list(point_list[1]),list(point_list[2])])
pts2 = np.float32([list(point_list[0]),list(point_list[1]),list(point_list[2])])

pts2[1][1] += 100 # 두번째 점의 Y 좌표를 아래로 이동


M = cv2.getAffineTransform(pts1,pts2)

img_result = cv2.warpAffine(img_original, M, (weight,height))


cv2.imshow("result1", img_result)
cv2.waitKey(0)



pts1 = np.float32([list(point_list[0]),list(point_list[1]),list(point_list[2])])
pts2 = np.float32([list(point_list[0]),list(point_list[1]),list(point_list[2])])

pts2[2][0] += 100 # 세번째 점의 X 좌료를 오른쪽으로 이동


M = cv2.getAffineTransform(pts1,pts2)

img_result = cv2.warpAffine(img_original, M, (weight,height))


cv2.imshow("result2", img_result)
cv2.waitKey(0)



pts1 = np.float32([list(point_list[0]),list(point_list[1]),list(point_list[2])])
pts2 = np.float32([list(point_list[0]),list(point_list[1]),list(point_list[2])])

pts2[1][1] += 100 # 두번째 점의 Y 좌표를 아래로 이동
pts2[2][0] += 50  # 세번째 점의 X 좌료를 오른쪽으로 이동


M = cv2.getAffineTransform(pts1,pts2)

img_result = cv2.warpAffine(img_original, M, (weight,height))


cv2.imshow("result3", img_result)
cv2.waitKey(0)


cv2.destroyAllWindows()

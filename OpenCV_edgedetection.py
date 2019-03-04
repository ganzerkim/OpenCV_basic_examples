# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 18:32:36 2019

@author: ganze
"""

#에지 검출

#소벨에서는 X 방향 에지 검출과 Y 방향 에지 검출을 위해 별도의 커널을 사용합니다.



import cv2


img_color = cv2.imread('2.bmp', cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

#convertScaleAbs 함수를 사용하여 sobel x 결과에 절대값을 적용하고 값 범위를 8비트 unsigned int로 변경해줘야합니다.
#소벨의 커널 크기가 3인 경우에는 Sobel 함수 대신에 Scharr 함수를 사용하는 것이 더 좋은 결과를 얻을 수 있다고 합니다. 

img_sobel_x = cv2.Sobel(img_gray, cv2.CV_64F, 1, 0, ksize=3)
img_sobel_x = cv2.convertScaleAbs(img_sobel_x)

img_sobel_y = cv2.Sobel(img_gray, cv2.CV_64F, 0, 1, ksize=3)
img_sobel_y = cv2.convertScaleAbs(img_sobel_y)


img_sobel = cv2.addWeighted(img_sobel_x, 1, img_sobel_y, 1, 0);


cv2.imshow("Sobel X", img_sobel_x)
cv2.imshow("Sobel Y", img_sobel_y)
cv2.imshow("Sobel", img_sobel)

cv2.waitKey(0)
cv2.destroyAllWindows()
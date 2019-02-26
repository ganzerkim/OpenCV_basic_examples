# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 22:46:01 2019

@author: ganze
"""

# Harris Corner Detection

#평평한 영역에서는 모든 방향으로 픽셀 강도 변화가 없다.
#에지에서는 에지의 방향따라 픽셀 강도 변화가 없고 에지와 수직방향으로 픽셀 강도 변화가 있다.
#코너에서는 모든 방향에 대해 강한 픽셀 강도 변화가 존재한다.  

import cv2  
import numpy as np  
  
image = cv2.imread('line.jpg')  
img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
img_gray = np.float32(img_gray)  
  
dst = cv2.cornerHarris( img_gray, 4, 3, 0.04 )  
  
image[dst>0.01*dst.max()] = [0,0,255]  
  
cv2.imshow('dst', image)  
cv2.waitKey(0) 

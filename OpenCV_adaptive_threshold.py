# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:04:34 2019

@author: ganze
"""

#adaptive thresholding

import cv2
import mpldatacursor
import matplotlib.pyplot as plt

img_source = cv2.imread('2.bmp', 0)


fig, ax = plt.subplots()
ax.imshow(img_source, interpolation='none')

mpldatacursor.datacursor(hover=True, bbox=dict(alpha=1, fc='w'))

plt.show()

#cv.ADAPTIVE_THRESH_MEAN_C : threshold value is the mean of neighbourhood area.
#cv.ADAPTIVE_THRESH_GAUSSIAN_C : threshold value is the weighted sum of neighbourhood values where weights are a gaussian window.
ret,img_result1 = cv2.threshold(img_source, 127, 255, cv2.THRESH_BINARY)
img_result2 = cv2.adaptiveThreshold(img_source, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 5)
img_result3 = cv2.adaptiveThreshold(img_source, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 5)



cv2.imshow("SOURCE", img_source)
cv2.imshow("THRESH_BINARY", img_result1)
cv2.imshow("ADAPTIVE_THRESH_MEAN_C", img_result2)
cv2.imshow("ADAPTIVE_THRESH_GAUSSIAN_C", img_result3)

cv2.waitKey(0)
cv2.destroyAllWindows()
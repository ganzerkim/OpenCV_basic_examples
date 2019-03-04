# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 14:25:52 2019

@author: ganze
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import mpldatacursor

img_source = cv2.imread('binary_test.png',0)

fig, ax = plt.subplots()
ax.imshow(img_source, interpolation='none')

ret,img_result1 = cv2.threshold(img_source, 127, 255, cv2.THRESH_BINARY)
ret,img_result2 = cv2.threshold(img_source, 127, 255, cv2.THRESH_BINARY_INV)


mpldatacursor.datacursor(hover=True, bbox=dict(alpha=1, fc='w'))


cv2.imshow("SOURCE", img_source)
cv2.imshow("THRESH_BINARY", img_result1)
cv2.imshow("THRESH_BINARY_INV", img_result2)

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
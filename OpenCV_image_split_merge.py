# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 20:46:18 2019

@author: ganze
"""

#image channel split & merge

import cv2
import numpy as np

img_color = cv2.imread('billard.png', cv2.IMREAD_COLOR )

img_b,img_g,img_r = cv2.split(img_color)

zeros = np.zeros((img_color.shape[0], img_color.shape[1]), dtype="uint8")
img_b = cv2.merge([img_b, zeros, zeros])
img_g = cv2.merge([zeros, img_g, zeros])
img_r = cv2.merge([zeros, zeros, img_r])

cv2.imshow("BGR", img_color)
cv2.imshow("B", img_b)
cv2.imshow("G", img_g)
cv2.imshow("R", img_r)

cv2.waitKey(0)

cv2.destroyAllWindows()
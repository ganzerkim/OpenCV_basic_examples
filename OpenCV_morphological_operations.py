# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 16:47:38 2019

@author: ganze
"""

#모폴로지 연산(Morphological Operations)

###########################################################
#Erosion
#바이너리 이미지에서 흰색 오브젝트의 외곽 픽셀을 0(검은색)으로 만듭니다. 
#노이즈(작은 흰색 물체)를 제거하거나 붙어 있는 오브젝트들을 분리하는데 사용할 수 있습니다.

import cv2
import numpy as np


img = cv2.imread('j.png',0)

#사용한 커널의 크기에 따라  오브젝트 외곽에서 0이 되는 픽셀의 정도가 달라집니다. 
#커널의 크기를 특정 크기(3, 3)으로 고정하고  Erosion 반복 횟수를 증가시켜서도 오브젝트 외곽에서 0이 되는 픽셀의 정도를 조절할 수 있습니다.
kernel = np.ones((5, 5), np.uint8)
result = cv2.erode(img, kernel, iterations = 1)

cv2.imshow("Source", img)
cv2.imshow("Result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()


###############################################################


#Dilation
#Erosion과 반대로 동작합니다. 바이너리 이미지에서 흰색 오브젝트의 외곽 픽셀 주변에 1(흰색)으로 추가합니다. 
#노이즈(작은 흰색 오브젝트)를 없애기 위해 사용한 Erosion에 의해서 작아졌던 오브젝트를 원래대로 돌리거나 인접해 있는 오브젝트들을 하나로 만드는데 사용할 수 있습니다. 


import cv2
import numpy as np


img = cv2.imread('j.png',0)

kernel = np.ones((5, 5), np.uint8)
result = cv2.dilate(img, kernel, iterations = 1)

cv2.imshow("Source", img)
cv2.imshow("Result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()

##############################################################

# Opening
#Erosion 연산 다음에 Dilation 연산을 적용합니다.  이미지 상의 노이즈(작은 흰색 물체)를 제거하는데 사용합니다. 
#노이즈(작은 흰색 오브젝트)를 없애기 위해 사용한 Erosion에 의해서 작아졌던 오브젝트에 Dilation 를 적용하면  오브젝트가 원래 크기로 돌아오게 됩니다.  



import cv2
import numpy as np


img = cv2.imread('j-noise.png',0)

kernel = np.ones((5, 5), np.uint8)
result = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

cv2.imshow("Source", img)
cv2.imshow("Result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()

#################################################################

#Closing

#Opening과 반대로 Dilation 연산을 먼저 적용한 후,  Erosion 연산을 적용합니다.
#희색 오브젝트에 있는 작은 검은색 구멍들을 메우는데 사용합니다.


import cv2
import numpy as np


img = cv2.imread('man.png',0)

kernel = np.ones((11, 11), np.uint8)
result = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

cv2.imshow("Source", img)
cv2.imshow("Result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()

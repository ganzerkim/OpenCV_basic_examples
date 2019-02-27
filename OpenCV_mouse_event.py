# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 21:51:38 2019

@author: ganze
"""

#마우스 이벤트 예제

import numpy as np
import cv2 as cv


mouse_event_types = { 0:"cv.EVENT_MOUSEMOVE", 1:"cv.EVENT_LBUTTONDOWN", 2:"cv.EVENT_RBUTTONDOWN", 3:"cv.EVENT_MBUTTONDOWN",
                 4:"cv.EVENT_LBUTTONUP", 5:"cv.EVENT_RBUTTONUP", 6:"cv.EVENT_MBUTTONUP",
                 7:"cv.EVENT_LBUTTONDBLCLK", 8:"cv.EVENT_RBUTTONDBLCLK", 9:"cv.EVENT_MBUTTONDBLCLK",
                 10:"cv.EVENT_MOUSEWHEEL", 11:"cv.EVENT_MOUSEHWHEEL"}

mouse_event_flags = { 0:"None", 1:"cv.EVENT_FLAG_LBUTTON", 2:"cv.EVENT_FLAG_RBUTTON", 4:"cv.EVENT_FLAG_MBUTTON",

                8:"cv.EVENT_FLAG_CTRLKEY", 9:"cv.EVENT_FLAG_CTRLKEY + cv.EVENT_FLAG_LBUTTON",
                10:"cv.EVENT_FLAG_CTRLKEY + cv.EVENT_FLAG_RBUTTON", 11:"cv.EVENT_FLAG_CTRLKEY + cv.EVENT_FLAG_MBUTTON",

                16:"cv.EVENT_FLAG_SHIFTKEY", 17:"cv.EVENT_FLAG_SHIFTKEY + cv.EVENT_FLAG_LBUTTON",
                18:"cv.EVENT_FLAG_SHIFTLKEY + cv.EVENT_FLAG_RBUTTON", 19:"cv.EVENT_FLAG_SHIFTKEY + cv.EVENT_FLAG_MBUTTON",

                32:"cv.EVENT_FLAG_ALTKEY", 33:"cv.EVENT_FLAG_ALTKEY + cv.EVENT_FLAG_LBUTTON",
                34:"cv.EVENT_FLAG_ALTKEY + cv.EVENT_FLAG_RBUTTON", 35:"cv.EVENT_FLAG_ALTKEY + cv.EVENT_FLAG_MBUTTON"}


# 마우스 이벤트 발생시 호출될 함수를 정의
def mouse_callback(event, x, y, flags, param):
    print(flags)
    print( '( '+ str(x) + ' ' + str(y), ')' + ' ' + mouse_event_types[event], end=" " )

    if event == 10:
        if flags > 0:
            print("forward scrolling", end=" " )
        else:
            print("backward scrolling", end=" ")
    elif event == 11:
        if flags > 0:
            print("right scrolling", end=" " )
        else:
            print("left scrolling", end=" ")
    else:
        print( mouse_event_flags[flags], end=" " )

    print(str(param))
    
    
img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow('image') #마우스 이벤트를 감지할 윈도우를 생성.

# 이름이 image인 윈도우에서 마우스 이벤트가 밸생하면 mouse_callback 함수가 호출됨.
cv.setMouseCallback('image', mouse_callback)

while(1):
    cv.imshow('image', img)
    
    k = cv.waitKey(1) & 0xFF
    
    if k == 27:
        print("esc 키 눌러짐")
        break
    
cv.destroyAllWindows()

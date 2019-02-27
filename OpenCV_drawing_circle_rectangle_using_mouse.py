# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 23:07:31 2019

@author: ganze
"""

#마우스로 원/사각형 그리기

import numpy as np   # for zeros
import cv2 as cv
import random        # for randrange


mouse_is_pressing = False   # 왼쪽 마우스 버튼 상태 체크를 위해 사용
drawing_mode = True       # 현재 그리기 모드 선택을 위해 사용 ( 원 / 사각형 )
start_x, start_y = -1, -1   # 최초로 왼쪽 마우스 버튼 누른 위치를 저장하기 위해 사용
color = (255, 255, 255)   # 도형 내부 채울때 사용할 색 지정시 사용 ( 초기값은 흰색 )




def mouse_callback(event,x,y,flags,param):

    global color, start_x, start_y, drawing_mode, mouse_is_pressing

    if event == cv.EVENT_RBUTTONDOWN:
        # 랜덤으로 (blue, green, red)로 사용될 색을 생성
        color = (random.randrange(256), random.randrange(256), random.randrange(256)) 


    elif event == cv.EVENT_MOUSEMOVE: 
        if mouse_is_pressing == True: # 마우스 왼쪽 버튼을 누른 채 이동하면 

            if drawing_mode == True: # 이동된 마우스 커서 위치를 반영하여 사각형/윈을 그림
                cv.rectangle(img,(start_x,start_y),(x,y),color,-1)
            else:
                cv.circle(img, (start_x,start_y), max(abs(start_x - x), abs(start_y - y)), color, -1)


    elif event == cv.EVENT_LBUTTONDOWN:

        mouse_is_pressing = True     # 왼쪽 마우스 버튼을 누른 것 감지 
        start_x, start_y = x, y     # 최초로 왼쪽 마우스 버튼 누른 위치를 저장 


    elif event == cv.EVENT_LBUTTONUP: 

        mouse_is_pressing = False    # 왼쪽 마우스 버튼에서 손뗀 것을 감지   

        if drawing_mode == True:  # 최종 위치에 마우스 커서 위치를 반영하여 사각형/윈을 그림
            cv.rectangle(img,(start_x,start_y),(x,y),color,-1)
        else:
            cv.circle(img, (start_x,start_y), max(abs(start_x - x), abs(start_y - y)), color, -1)



img = np.zeros((512, 512, 3), np.uint8) 
cv.namedWindow('image')   
cv.setMouseCallback('image', mouse_callback) 


while(1):

    cv.imshow('image',img)

    k = cv.waitKey(1) & 0xFF

    if k == ord('m'): # m 누르면 그리기 모드 변경( 사각형 / 원 ) 
        drawing_mode = not drawing_mode

    elif k == 27: 
        break

cv.destroyAllWindows() 

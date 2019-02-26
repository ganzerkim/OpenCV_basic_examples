# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 22:55:46 2019

@author: ganze
"""
#동영상 다루기

import cv2

"""
#argument가 0인 비디오 캡쳐 불러옴
capture = cv2.VideoCapture(0)

#카메라로 부터 이미지 한장을 가져옴
ret, img_color = capture.read()


#가져온 이미지 띄우기
cv2.imshow("color", img_color)


#아무키나 누를때까지 대기
cv2.waitKey(0)

capture.release
cv2.destroyAllWindows()
"""
"""
#====>이를 반복하면 동영상이 됨.

#argument가 0인 비디오 캡쳐 불러옴
capture = cv2.VideoCapture(0)

#사용할 코덱 추가적으로 지정
fourcc = cv2.VideoWriter_fourcc(*'XVID')

#비디오 저장(저장이름, 사용될 코덱, 초당프레임 수, 영상 사이즈(캡쳐되는 사이즈와 일치시켜야함))

writer = cv2.VideoWriter('output.avi', fourcc, 30.0, (640, 480))

while(True):
    #카메라로 부터 이미지 한장을 가져옴
    ret, img_color = capture.read()

    # 캡쳐가 실행되지 않은 경우 다시 첫줄부터 시작
    if ret == False:
        continue
    
    #컬러이미지 그레이스케일로 변환
    
    img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
    
    #가져온 이미지 띄우기
    cv2.imshow("color", img_color)
    cv2.imshow("Gray", img_gray)

    #카메라로 부터 반복적으로 캡쳐된 영상을 모아 동영상으로 만듬
    writer.write(img_color)
    #esc 키 누르면 무한루프에서 빠져나오게 하기
    #키보드 입력을 받기 위해 1초 후 키를 받음.
    if cv2.waitKey(1)&0xFF == 27:
        break

capture.release
writer.release

cv2.destroyAllWindows()
"""

#argument가 재생할 동영상 불러옴
capture = cv2.VideoCapture("output.avi")

#사용할 코덱 추가적으로 지정
fourcc = cv2.VideoWriter_fourcc(*'XVID')

#비디오 저장(저장이름, 사용될 코덱, 초당프레임 수, 영상 사이즈(캡쳐되는 사이즈와 일치시켜야함))



while(True):
    #카메라로 부터 이미지 한장을 가져옴
    ret, img_color = capture.read()

    # 캡쳐가 실행되지 않은 경우 다시 첫줄부터 시작
    #동영상이 끝까지 재생되면 무한루프에서 빠져나오게 함.
    if ret == False:
        break
    
    #컬러이미지 그레이스케일로 변환
    
    img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
    
    #가져온 이미지 띄우기
    cv2.imshow("color", img_color)
    cv2.imshow("Gray", img_gray)

    #카메라로 부터 반복적으로 캡쳐된 영상을 모아 동영상으로 만듬
    
    #esc 키 누르면 무한루프에서 빠져나오게 하기
    #키보드 입력을 받기 위해 1초 후 키를 받음.
    if cv2.waitKey(1)&0xFF == 27:
        break

capture.release


cv2.destroyAllWindows()
 
 

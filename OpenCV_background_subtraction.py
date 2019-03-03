# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 21:17:52 2019

@author: ganze
"""

# 테스트 동영상 출처 - http://www.cvc.uab.es/~bagdanov/master/videos/car-overhead-1.avi

import cv2
import numpy as np



cap = cv2.VideoCapture("car-overhead-1.avi")

# 옵션 설명 http://layer0.authentise.com/segment-background-using-computer-vision.html
fgbg = cv2.createBackgroundSubtractorMOG2(varThreshold=100)


while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)



    nlabels, labels, stats, centroids = cv2.connectedComponentsWithStats(fgmask)


    for index, centroid in enumerate(centroids):
        if stats[index][0] == 0 and stats[index][1] == 0:
            continue
        if np.any(np.isnan(centroid)):
            continue


        x, y, width, height, area = stats[index]
        centerX, centerY = int(centroid[0]), int(centroid[1])

        if area > 100:
            cv2.circle(frame, (centerX, centerY), 1, (0, 255, 0), 2)
            cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 0, 255))


    cv2.imshow('mask',fgmask)
    cv2.imshow('frame',frame)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

"""
import cv2
import numpy as np



cap = cv2.VideoCapture("Cam1_Indoor.avi")

# 옵션 설명 http://layer0.authentise.com/segment-background-using-computer-vision.html
fgbg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=500, detectShadows=0)


while(1):
    ret, frame = cap.read()

    width = frame.shape[1]
    height = frame.shape[0]
    frame = cv2.resize(frame, (int(width*0.5), int(height*0.5)))



    fgmask = fgbg.apply(frame)



    nlabels, labels, stats, centroids = cv2.connectedComponentsWithStats(fgmask)


    for index, centroid in enumerate(centroids):
        if stats[index][0] == 0 and stats[index][1] == 0:
            continue
        if np.any(np.isnan(centroid)):
            continue


        x, y, width, height, area = stats[index]
        centerX, centerY = int(centroid[0]), int(centroid[1])

        if area > 10:
            cv2.circle(frame, (centerX, centerY), 1, (0, 255, 0), 2)
            cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 0, 255))


    cv2.imshow('mask',fgmask)
    cv2.imshow('frame',frame)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
"""
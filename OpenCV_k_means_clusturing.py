# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 21:04:28 2019

@author: ganze
"""

#K-Means Clusturing
#데이터 전체를 여러개의 그룹으로 만들때 사용하는 것
# 이 알고리즘은 반복적인 처리 알고리즘임.
# 1단계 : 알고리즘은 임의로 두 개의 중심점(centroid)인 C1과 C2를 선택한다.   C1, C2 ( 중심 점으로 두 개의 데이터를 선택하기도 한다. )
# 2단계 : 두 개의 중심점으로 부터 각 점들까지의 거리를 계산한다.  C1에 가까운 데이터엔 0으로 이름 붙이고 C2에 가까운 데이터엔 1이라고 이름을 붙인다.
# 이미지상에서는 0으로 라벨붙인 점들은 빨간색, 1로 라벨붙인 점들은 파란색으로 표현되었다.
# 3단계 :  빨간 점들과 파란점 들의 좌표들에 대해 각각 평균점을 구한다. 이점이 새로운 C1과 C2가 된다. 
# 다시 2단계를 반복한다. 아래 그림은 새로운 평균점이 이동한 후.. 다시 가까운쪽 중심점에 속하는 점들을 나눈 결과이다. 
# 2단계와 3단계를 계속 반복한다. 중심점이 더 이상 이동하지 않으면 반복이 종료된다.

# (C1 중심점과 빨간색 점들간의 거리의 합  + C2중심점과 파란색 점들간의 거리의 합 ) 이 최소가 되는 것을 찾으면 종료되는 것이다. 
# 최종적으로는 아래와 같이 두 그룹으로 나누어 질것이다.

# 10번 반복하거나 정확도(accuracy of epsilon)가 1.0에 도달했을때 반복을 중단하고 결과를 내놓도록 기준을 정해서 태스트하는 예제이다.

import numpy as np  
import cv2  
from matplotlib import pyplot as plt  
  
#25~50사이의 숫자를 랜덤으로 2차원 데이터 (x,y) 25개 뽑음  
a = np.random.randint(25,50,(25,2))  
  
#60~85사이의 숫자를 랜덤으로 랜덤으로 2차원 데이터 (x,y) 25개 뽑음  
b = np.random.randint(55,85,(25,2))  
  
#수직방향으로 값들을 넣어준다.  
z = np.vstack((a,b))  
  
#float32타입으로 데이터를 변경한다.  
z=np.float32(z)  
  
 # Define criteria = ( type, max_iter = 10 , epsilon = 1.0 )  
criteria = (cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,10,1.0)  
  
#초기 중심점을 랜덤으로 정한다.  
#flags = cv2.KMEANS_RANDOM_CENTERS  

#KMeans를 적용한다. k=2, 10번 반복한다.  
#compactness,labels,centers = cv2.kmeans( z, 2, criteria, 10, flags )  
# define criteria and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
ret, labels, centers = cv2.kmeans(z,2,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

  
#라벨을 보고 데이터를 두 그룹으로 나눈다.  
A = z[labels.ravel()==0]  
B = z[labels.ravel()==1]  
  
#화면에 출력  
plt.scatter(A[:,0], A[:,1], c='b')  
plt.scatter(B[:,0], B[:,1], c='r')  
plt.scatter( centers[:,0], centers[:,1], s=80, c='y', marker='s')  
  
plt.xlabel('Height')  
plt.ylabel('Weight')  
plt.show()  


# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 23:16:31 2019

@author: ganze
"""

import numpy as np
import cv2
import pydicom as dicom

ds=dicom.dcmread('sample.IMA')
dcm_sample=ds.pixel_array * 128
cv2.imshow('sample image dicom',dcm_sample)


while(True):
    if cv2.waitKey(1)& 0xFF == 27:
        break
cv2.destroyAllWindows()
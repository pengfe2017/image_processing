# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 08:15:30 2019

@author: 李鹏飞
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

#%% Function for creating a image data

def SingleModeImageCreate(MatrixDimension = 1000, Frequency = 10):
    TotalTime = 12
    omega = Frequency
    RowData = np.linspace(0,TotalTime,MatrixDimension)
    SinRowData = np.sin(omega*RowData)
    SinRowData = ((SinRowData+1)*255/2).astype(float)    
    #%form an array
    imgArray = []
    for idx in range(1000):
        imgArray.append(SinRowData)   
    imgArray = np.array(imgArray)   
    return imgArray

#%% Creat an image

img = cv2.imread('messi5.jpg',0)

RowData = np.arange(0,1000,1)
RowData1 = np.linspace(0,12,1000)
omega = 10
SinRowData = np.sin(2*RowData1)
SinRowData = ((SinRowData+1)*255/2).astype(float)

#%form an array
imgArray = []
for idx in range(1000):
    imgArray.append(SinRowData)

imgArray = np.array(imgArray)

imgArrayTranspose = np.transpose(imgArray)

imgArrayTotal = imgArray + imgArrayTranspose
imgArrayTotal = 255*imgArrayTotal/imgArrayTotal.max()

RandomMatrix = np.random.rand(1000,1000)*100

plt.plot(RowData1,SinRowData)

#%% dft the images
ImgforProcessing = imgArrayTotal
for i in range(10):
    ImgforProcessing = ImgforProcessing + SingleModeImageCreate(1000,i*2)
    ImgforProcessing = 255*ImgforProcessing/ImgforProcessing.max()
    

    
imgforProcessing = imgArrayTotal+ SingleModeImageCreate(1000,4)
ImgforProcessing = 255*ImgforProcessing/ImgforProcessing.max()


dft = cv2.dft(np.float32(ImgforProcessing),flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
#%%save image



cv2.imwrite("SavedigImg.jpg",imgArrayTotal/2)

#%% Plot img
plt.subplot(121),plt.imshow(ImgforProcessing, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()

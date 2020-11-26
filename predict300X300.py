# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 14:48:47 2020

@author: fsfil
"""


import cv2
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import os
import numpy as np



CATEGORIES = ["Normal","Pneumonia"]

def imgproc(filepath):
    IMG_SIZE = 300
    img_array = cv2.imread(filepath)
    new_array = cv2.resize(img_array, (IMG_SIZE,IMG_SIZE))
    plt.imshow(new_array)
    plt.show()
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)
    new_array = np.array(new_array)

model= tf.keras.models.load_model("D:\Pneumonia_CNN\VisorModel1.h5")

prediction = model.predict([imgproc("pne2.jpeg")])

print(CATEGORIES [int (prediction[0][0])])
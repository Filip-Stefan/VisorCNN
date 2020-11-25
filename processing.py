# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 11:31:43 2020

@author: fsfil
"""

import numpy as np
import os
import cv2
import matplotlib.pyplot as plt
import pickle
from PIL import Image
from resizeimage import resizeimage

DATADIR = "D:/Pneumonia_CNN/Test_data"
CATEGORIES = ["Normal", "Pneumonia"]

for category in CATEGORIES:
    path = os.path.join(DATADIR, category)
    for img in os.listdir(path):
        img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
        plt.imshow(img_array)
        plt.show()
        break
    break

IMG_SIZE = 300
new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
plt.imshow(new_array, cmap="gray")
plt.show()

training_data = []


# img = Image.open(fd_img)
# img = resizeimage.resize_contain(img, [200, 100])
# img.save('test-image-contain.jpeg', img.format)

def create_training_data():
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category)
        class_num = CATEGORIES.index(category)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                training_data.append([new_array, class_num])
            except Exception as e:
                pass


create_training_data();

import random

random.shuffle(training_data)

for sample in training_data:
    print(sample[0])

X = []  # feature set
y = []  # labels

for features, label in training_data:
    X.append(features)
    y.append(label)

X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)

pickle_out = open("X_val.pickle", "wb")
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out = open("y_val.pickle", "wb")
pickle.dump(y, pickle_out)
pickle_out.close()

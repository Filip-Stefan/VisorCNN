# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 16:32:03 2020

@author: fsfil
"""


import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
import pickle 
import os
import cv2
import numpy as np
from tensorflow.keras.callbacks import TensorBoard
import time



#salvare de logs
NAME = 'Pneumonia-300x300-model1-{}'.format(int(time.time()))
tensorboard = TensorBoard(log_dir = 'C:/Users/fsfil/logscnn2/{}'.format(NAME))

#declararea de variabile pentru training si labeing, luate din dataset-ul fafacut de primul soft
X = pickle.load(open("X_train.pickle","rb"))
y = pickle.load(open("y_train.pickle", "rb"))


X_val = pickle.load(open('X_val.pickle','rb'))
y_val = pickle.load(open('y_val.pickle','rb'))

#normalizarea valorilor din X( ex: 255/255 = 1)
X_val = X_val/255.0
X = X/255.0



#Layer I
#prima tura de Convolution + Pooling (trimite un set de date comprimat catre al doilea layer)
model = Sequential()
model.add(Conv2D(64,(3,3), input_shape = X.shape[1:]))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size = (2,2)))

#Layer II
#mai comprima inca o data datele trimise de layer-ul de sus si le pregateste pentru
#layer-ul de output
model.add(Conv2D(64,(3,3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size = (2,2)))
model.add(Dropout(0.2))


model.add(Conv2D(32,(3,3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size = (2,2)))
model.add(Dropout(0.1))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation("relu"))

#MA LAS DE FACULTALTE SI MA ANGAJEZ LA MC
#transformarea datelor dintr-un model bidimensional intr-unul unidimensional
model.add(Dense(1))
model.add(Activation("sigmoid"))

model.compile(loss = "binary_crossentropy", 
              optimizer = "adam", 
              metrics = ["accuracy"])

#model.fit(X, y, batch_size = 20, epochs = 1, validation_data =(X_val, y_val) , callbacks = [tensorboard])
model.save("model1.h5")
#model.evaluate(X_val,y_val,verbose=1)

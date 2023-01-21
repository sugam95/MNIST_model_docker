#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
import keras
from keras.models import Sequential
from keras.datasets import mnist
from keras.layers import Dense
from keras.optimizers import Adam
from keras.utils.np_utils import to_categorical 
import random
np.random.seed(0)

#loading data 
(X_train, y_train), (X_test, y_test) = mnist.load_data()
print(X_train.shape)
print(X_test.shape)
print(y_train.shape[0])

#look for the condition throw error otherwise
assert(X_train.shape[0] == y_train.shape[0]), "The number of images is not equal .."
assert(X_test.shape[0] == y_test.shape[0]), "The number of images is not equal .."
assert(X_train.shape[1:] == (28, 28)), "The dimension of the images are not 28x28"
assert(X_test.shape[1:] == (28, 28)), "The dimension of the images are not 28x28"


y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10) 


#Each image has Intensity from 0 to 255
X_train = X_train/255 
X_test = X_test/255

#Preprocessing data for model
num_of_classes = 10
num_pixels = 784
X_train = X_train.reshape(X_train.shape[0],num_pixels)
X_test = X_test.reshape(X_test.shape[0],num_pixels)
print(X_train.shape)



#model creation
def create_model():
  model = Sequential()
  model.add(Dense(10, input_dim = num_pixels,
                  activation = 'relu'))
  model.add(Dense(30, activation='relu'))
  model.add(Dense(10, activation='relu'))
  model.add(Dense(num_of_classes, activation='softmax'))
  model.compile(Adam(lr=0.01),
                loss='categorical_crossentropy',
               metrics=['accuracy'])
  return model

model = create_model()
print(model.summary())

#Training model
history = model.fit(X_train, y_train, validation_split=0.1,epochs=10, batch_size=200, verbose=1, shuffle=1)
model.save('final_model.h5')

#model evaluation
score = model.evaluate(X_test, y_test, verbose=0)
print('Test Accuracy:', score[1])
     


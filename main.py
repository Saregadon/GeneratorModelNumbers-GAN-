#if need keras >= 2.2
#python3.7 -m pip install keras==2.1.5

import numpy as np
import keras
import matplotlib
import tensorflow as tf
from matplotlib import pyplot
from keras.datasets.mnist import load_data


(trainX, trainy), (testX, testy) = load_data()
#define training data set

print('Train', trainX.shape, trainy.shape) #shows training amount
print('Test', testX.shape, testy.shape) #shows testing amount

for i in range(25):
    pyplot.imshow(trainX[i], cmap='gray')
    pyplot.subplot(5, 5, 1+i)
    pyplot.axis('off')
    pyplot.imshow(trainX[i], cmap='gray_r')
pyplot.show()

X = expand_dims(trainX, axis =-1)

X = X.astype('float32') #changing unsigned to float
X = X / 255.0 #normalizing data from [0, 255] to [0, 1]

print(tf.__version__)
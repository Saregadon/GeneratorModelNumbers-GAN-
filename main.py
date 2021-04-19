#if need keras >= 2.2
#python3.7 -m pip install keras==2.1.5

import numpy as np
import keras
import matplotlib
import tensorflow as tf
from matplotlib import pyplot
from keras.datasets.mnist import load_data

(trainX, trainy), (testX, testy) = load_data()

print('Train', trainX.shape, trainy.shape)
print('Test', testX.shape, testy.shape)

print(tf.__version__)
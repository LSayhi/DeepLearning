# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 14:37:58 2018

@author: BD
"""

import numpy as np
#np.random.seed(1337)  # for reproducibility
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.utils import np_utils
from keras import backend as K
import h5py


# 全局变量
batch_size = 128
nb_classes = 128
epochs = 20
# input image dimensions
img_rows, img_cols = 90, 90
# number of convolutional filters to use
nb_filters = 32
# size of pooling area for max pooling
pool_size = (2, 2)
# convolution kernel size
kernel_size = (3, 3)

# the data, shuffled and split between train and test sets


train_dataset = h5py.File('D:/codes/spyder/radar02/dataset.h5', 'r')
train_set_x_orig = np.array(train_dataset['X_train'][:]) # your train set features
train_set_y_orig = np.array(train_dataset['Y_train'][:]) # your train set labels
test_set_x_orig = np.array(train_dataset['X_test'][:]) # your train set features
test_set_y_orig = np.array(train_dataset['Y_test'][:]) # your train set labels

print("数据集已读入成功")
'''
# 根据不同的backend定下不同的格式
if K.image_dim_ordering() == 'th':
    X_train = X_train.reshape(X_train.shape[0], 1, img_rows, img_cols)
    X_test = X_test.reshape(X_test.shape[0], 1, img_rows, img_cols)
    input_shape = (1, img_rows, img_cols)
else:
    X_train = X_train.reshape(X_train.shape[0], img_rows, img_cols, 1)
    X_test = X_test.reshape(X_test.shape[0], img_rows, img_cols, 1)
    input_shape = (img_rows, img_cols, 1)
'''
input_shape = (img_rows, img_cols, 3)
X_train = train_set_x_orig.astype('float32')
X_test  = test_set_x_orig.astype('float32')
X_train /= 255
X_test  /= 255
print('X_train shape:', X_train.shape)
print(X_train.shape[0], 'train samples')
print(X_test.shape[0], 'test samples')
print("数据集归一化成功")

# 转换为one_hot类型
Y_train = np_utils.to_categorical(train_set_y_orig, nb_classes)
Y_test = np_utils.to_categorical(test_set_y_orig, nb_classes)
print("标签转换成one-hot成功")

#构建模型
model = Sequential()
"""
model.add(Convolution2D(nb_filters, kernel_size[0], kernel_size[1],
                        border_mode='same',
                        input_shape=input_shape))
"""
model.add(Convolution2D(nb_filters, (kernel_size[0], kernel_size[1]),
                        padding='same',
                        input_shape=input_shape)) # 卷积层1
model.add(Activation('relu')) #激活层
model.add(Convolution2D(nb_filters, (kernel_size[0], kernel_size[1]))) #卷积层2
model.add(Activation('relu')) #激活层
model.add(MaxPooling2D(pool_size=pool_size)) #池化层
#model.add(Dropout(0.25)) #神经元随机失活
model.add(Flatten()) #拉成一维数据
model.add(Dense(128)) #全连接层1
model.add(Activation('relu')) #激活层
#model.add(Dropout(0.5)) #随机失活
model.add(Dense(nb_classes)) #全连接层2
model.add(Activation('softmax')) #Softmax评分
print("模型构建成功")

#编译模型
'''
model.compile(loss='categorical_crossentropy',
              optimizer='adadelta',
              metrics=['accuracy'])
print("模型编译成功")
'''
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
print("模型编译成功")
#训练模型
model.fit(X_train, Y_train, batch_size=batch_size, epochs=epochs,
          verbose=1, validation_data=(X_test, Y_test))
print("模型训练结束")

#评估模型
scoretrain= model.evaluate(X_train, Y_train, verbose=0)
scoretest = model.evaluate(X_test, Y_test, verbose=0)
print('train score:', scoretrain[0])
print('train accuracy:', scoretrain[1])
print('Test score:', scoretest[0])
print('Test accuracy:', scoretest[1])
print("模型评估结束")
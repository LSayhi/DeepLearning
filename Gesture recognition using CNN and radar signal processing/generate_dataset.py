# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 13:43:37 2018

@author: BD
用自己的图片生成数据集
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import h5py
#导入必要的包
def get_files(file_dir):
    anniu = []
    label_anniu = []
    fanzhuan = []
    label_fanzhuan = []
    qianhou = []
    label_qianhou = []
    shangxia = []
    label_shangxia = []
        
    for file in os.listdir(file_dir):
        name = file.split(sep='.')
        if name[0]=='anniu':
            anniu.append(file_dir+file)
            label_anniu.append(0)
        elif name[0] == 'fanzhuan':
            fanzhuan.append(file_dir+file)
            label_fanzhuan.append(1)
        elif name[0]=='qianhou':
            qianhou.append(file_dir+file)
            label_qianhou.append(2)
        else:
            shangxia.append(file_dir+file)
            label_shangxia.append(3)
            
       #根据图片的名称，对图片进行提取，这里用.来进行划分
       ###一定要将分类的标签从0开始。这里是四类，标签为0，1，2，3。
       
    image_list = np.hstack((anniu, fanzhuan, qianhou, shangxia))
    label_list = np.hstack((label_anniu, label_fanzhuan, label_qianhou, label_shangxia))
 
    #利用shuffle打乱顺序
    temp = np.array([image_list, label_list])
    temp = temp.transpose()
    np.random.shuffle(temp)
 
    #从打乱的temp中再取出list（img和lab）
    image_list = list(temp[:, 0])
    label_list = list(temp[:, 1])
    label_list = [int(i) for i in label_list] 
    print("图像标签化完成")
    return  image_list,label_list
    #返回两个list 分别为图片文件名及其标签  顺序已被打乱
    
train_dir = 'D:/codes/spyder/radar02/dataset_RGB_Resize/'
image_list,label_list = get_files(train_dir)
 
print('The length of train images'+str(len(image_list)))
print('The length of train labels'+str(len(label_list)))


#初始化数据集大小
m=len(image_list)#数据集总个数
m_train=int(0.8*m)#训练集占80%
m_test=m-m_train  #测试集占20%

Train_image =  np.random.rand(m_train, 90, 90, 3).astype('float32')
Train_label = np.random.rand(m_train, 1).astype('float32')
 
Test_image =  np.random.rand(m_test, 90, 90, 3).astype('float32')
Test_label = np.random.rand(m_test, 1).astype('float32')


  
#给数据集赋值
for i in range(m_train):
    Train_image[i] = np.array(plt.imread(image_list[i]))
    Train_label[i] = np.array(label_list[i])
 
for i in range(m_train,m):
    Test_image[i+m_test-m] = np.array(plt.imread(image_list[i]))
    Test_label[i+m_test-m] = np.array(label_list[i])

 
# Create a new file
f = h5py.File('dataset.h5', 'w')
f.create_dataset('X_train', data=Train_image)
f.create_dataset('Y_train', data=Train_label)
f.create_dataset('X_test', data=Test_image)
f.create_dataset('Y_test', data=Test_label)
print("生成.h5数据集成功")

#测试
# Load hdf5 dataset
train_dataset = h5py.File('dataset.h5', 'r')
train_set_x_orig = np.array(train_dataset['X_train'][:]) # your train set features
train_set_y_orig = np.array(train_dataset['Y_train'][:]) # your train set labels
test_set_x_orig = np.array(train_dataset['X_test'][:]) # your train set features
test_set_y_orig = np.array(train_dataset['Y_test'][:]) # your train set labels


print(train_set_x_orig.shape)
print(train_set_y_orig.shape)
print(test_set_x_orig.shape)
print(test_set_y_orig.shape)


plt.imshow(train_set_x_orig[1])
print(train_set_y_orig[1])
print("完成测试，数据集制作成功，已保存.h5文件")
f.close()

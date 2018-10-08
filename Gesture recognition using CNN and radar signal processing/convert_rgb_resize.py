# -*- coding: 将图像转换为3通道RGB形式 -*-
"""
Created on Tue Sep 18 15:26:43 2018

@author: LSayhi
"""
import os
from PIL import Image

#转换成三通道
def AlltoRGB(file_dir,new_dir,width,heigth):
    for filename in os.listdir(file_dir):
        im=Image.open(file_dir+filename).convert("RGB").resize((width,heigth))
        im.save(new_dir+filename)
        #想要保存的路径
    print("已转换RGB格式，图像大小"+"("+str(width)+","+str(heigth)+","+"3"")")
'''
def resize(file_dir,m,n):
    for filename in os.listdir(file_dir):
        im=Image.open()
    pic = Image.open(root)
    pic = pic.resize((220, 220))
    print("resize完成")
'''
def main():
    file_dir="D:/codes/spyder/radar02/dataset/"#原图像路径
    new_dir ="D:/codes/spyder/radar02/dataset_RGB_Resize/"#保存到新的地址
    width=90
    heigth=90
    AlltoRGB(file_dir,new_dir,width,heigth)
    

if __name__ == '__main__':
    main()
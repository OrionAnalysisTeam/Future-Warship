# -*- coding: utf-8 -*-
"""
===============================================
Project Name:筛选速度为0的数据
Working with Python
-----------------------------------------------
Developer:
Operate:--Orion Analysis Team--
Program:--Vector Data Analysis Team--
...............................................
Author(Analyst):朱立松--Mr.Zhu--
The Chief of Teams
===============================================

"""

import pandas as pd
import numpy as np
import os

for name in os.listdir('E:/the_data/our_new_data_tidu'): 
    domain = os.path.abspath(r'E:/the_data/our_new_data_tidu') #获取文件夹的路径 
    info = os.path.join(domain,name) #将路径与文件名结合起来就是每个文件的完整路径 
    data = pd.read_csv(info) #读取csv数据文件
    print('已成功读取数据')
    
    #开始选取速度为0的数据
    zero_data = data[data['gps_speed']==0]
    print('已锁定速度为0的数据区块')
    no_zero_data = data[data['gps_speed']!=0]
    print('已锁定速度不为0的数据区块')
    
    file_name = str('E:/the_data/zero_data/{}'.format(name)) #设置速度为0文件及路径名
    another_name = str('E:/the_data/no_zero_data/{}'.format(name)) #设置速度不为0文件及路径名
    zero_data.to_csv(file_name) #输出
    print('已完成输出速度为0的数据文件{}'.format(name))
    
    no_zero_data.to_csv(another_name)
    print('已完成输出速度不为0的数据文件{}'.format(name))
    
print('速度为0的数据文件位于“D:/the_data/zero_data/”')
print('速度不为0的数据文件位于”D:/the_data/no_zero_data/“')
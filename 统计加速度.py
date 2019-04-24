# -*- coding: utf-8 -*-
"""
===============================================
Project Name:
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

alist = []
with open('E:/the_data/tongji.txt',"a+") as log_writter:
    

    for name in os.listdir('E:/the_data/best_data_B/best_data_B'): 
    
        domain = os.path.abspath(r'E:/the_data/best_data_B/best_data_B') #获取文件夹的路径 
        info = os.path.join(domain,name) #将路径与文件名结合起来就是每个文件的完整路径 
        data = pd.read_csv(info) #读取csv数据文件
        print('正在处理文件{}'.format(name))
        dayu = data[data['jiasudu']>=3]
        print('已锁定加速度大于3的区块')
        xiaoyu = data[data['jiasudu']<=-3]
        print('已锁定加速度小于-3的区块')
        
        a = len(dayu['jiasudu'])
        b = len(xiaoyu['jiasudu'])
        
        print('文件{0}中加速度大于3的总数量为：{1}'.format(name,a))
        log_writter.write(str('{0}中加速度大于3的数量为{1}''\n'.format(name,a)))
        print('文件{0}中加速度小于-3的总数量为：{1}'.format(name,b))
        log_writter.write(str('{0}中加速度小于-3的数量为{1}''\n'.format(name,b)))
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
with open('E:/the_data/tjdaisu.txt',"a+") as log_writter:
    
    for name in os.listdir('E:/the_data/the_all_data/thedata'): 
    
        domain = os.path.abspath(r'E:/the_data/the_all_data/thedata') #获取文件夹的路径 
        info = os.path.join(domain,name) #将路径与文件名结合起来就是每个文件的完整路径 
        data = pd.read_csv(info) #读取csv数据文件
        print('已读取数据文件{}'.format(name))
        acc_state = data['acc_state']
        gps_speed = data['gps_speed']
        accadds = acc_state + gps_speed
        adir = {'accadds':list(accadds)}
        accadds = pd.DataFrame(adir)
        print('已求出状态与速度之和')
        data = pd.concat([data,accadds],axis=1)
        print('已建立新的数据表格')
        
        file_name = str('E:/the_data/best_data_D/{}'.format(name)) #设置文件及路径名
        data.to_csv(file_name) #输出
        print('已输出新文件{}'.format(name))
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
Author(Analyst):--Mr.Zhu--
The Chief of Teams
===============================================

"""
import os
import pandas as pd
import numpy as np


for name in os.listdir('E:/the_data/the_all_data/thedata'): 
    domain = os.path.abspath(r'E:/the_data/the_all_data/thedata') #获取文件夹的路径 
    info = os.path.join(domain,name) #将路径与文件名结合起来就是每个文件的完整路径 
    data = pd.read_csv(info) #读取csv数据文件
    new_data = data.drop_duplicates(['lng','lat'],keep='last') #删除经度、维度完全相同的点
    file_name = str('E:/the_data/new_data/{}'.format(name)) #设置文件及路径名
    new_data.to_csv(file_name) #输出
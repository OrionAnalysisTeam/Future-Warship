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
import pandas as pd
import numpy as np
import os



for name in os.listdir('E:/the_data/new_data'): 
    domain = os.path.abspath(r'E:/the_data/new_data') #获取文件夹的路径 
    info = os.path.join(domain,name) #将路径与文件名结合起来就是每个文件的完整路径 
    data = pd.read_csv(info) #读取csv数据文件
    data =data[~data['delta_jingdu'].isin([0])]
    delta_jingdu = data['delta_jingdu'].copy()
    delta_weidu = data['delta_weidu'].copy()
    x = len(delta_jingdu)
    list_tidu = []
    list_tidu.append(0)
    for i in range(1,x):
        tidu_abs = np.abs(delta_weidu/delta_jingdu)
        list_tidu.append(tidu_abs)
    tidu_abs = {'tidu_abs':tidu_abs}
    tidu_abs = pd.DataFrame(tidu_abs)
    data = pd.concat([data,tidu_abs],axis=1)

    file_name = str('E:/the_data/new_data_tidu/{}'.format(name)) #设置文件及路径名
    data.to_csv(file_name) #输出

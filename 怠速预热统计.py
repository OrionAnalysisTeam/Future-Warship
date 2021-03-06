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
with open('E:/the_data/tjdaisu.txt',"a+") as log_writter:
    for name in os.listdir('E:/the_data/best_data_C'): 
    
        domain = os.path.abspath(r'E:/the_data/best_data_C') #获取文件夹的路径 
        info = os.path.join(domain,name) #将路径与文件名结合起来就是每个文件的完整路径 
        data = pd.read_csv(info) #读取csv数据文件
        print('已读取数据文件{}'.format(name))
        the_list = []
        k = 1
        print('准备遍历{}的数据'.format(name))
        for i in range(1,len(data['accadds'])):
            if data['accadds'][i] == data['accadds'][i-1] == 1: #判断是否前一项与后一项都为1
                if data['accadds'][i-1]<=1:   #如果是，判断是否前一项小于等于1
                    k = k+1     #如果是，统计累加
                    if data['accadds'][i]>=1:   #判断是否该项大于1
                        if k > 30 :  #如果是，判断累加是否大于30
                            the_list.append(k)   #如果是，将累加填入队列中
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
            else:
                continue
        number = len(the_list)
        print('文件{0}中怠速预热超过30秒的次数为：{1}'.format(name,number))
        log_writter.write(str('文件{0}怠速预热超过30秒的次数为：{1}''\n'.format(name,number)))
            
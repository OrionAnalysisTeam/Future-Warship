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
import datetime as dt
import dateutil
with open('E:/the_data/xihuohuaxing.txt',"a+") as log_writter:
    for name in os.listdir('E:/the_data/the_all_data/thedata'): 
    
        domain = os.path.abspath(r'E:/the_data/the_all_data/thedata') #获取文件夹的路径 
        info = os.path.join(domain,name) #将路径与文件名结合起来就是每个文件的完整路径 
        data = pd.read_csv(info) #读取csv数据文件
        print('已读取数据文件{}'.format(name))
        the_list = []
        k = 0
        delta = dt.timedelta(0,0)
        print('准备遍历{}的数据'.format(name))
        for i in range(1,len(data['acc_state'])):
            if data['acc_state'][i-1] == 0:  #如果前一项为0
                if data['acc_state'][i] == 0:#如果该项为0
                    if data['gps_speed'][i-1] > 0:
                        a = dateutil.parser.parse(data['location_time'][i])-dateutil.parser.parse(data['location_time'][i-1])
                        delta = delta + a
                else:
                    if delta > dt.timedelta(0,3):
                        the_list.append(delta)
                        delta = dt.timedelta(0,0)
                    else:
                        delta = dt.timedelta(0,0)
                        continue
            else:
                continue

        number = len(the_list)
        print('文件{0}熄火滑行大于3秒的次数为：{1}'.format(name,number))
        log_writter.write(str('文件{0}熄火滑行大于3秒的次数为：{1}''\n'.format(name,number)))
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
with open('E:/the_data/panduanjieguo.txt',"a+") as log_writter:
    

    for name in os.listdir('E:/the_data/the_all_data/thedata'): 
    
        domain = os.path.abspath(r'E:/the_data/the_all_data/thedata') #获取文件夹的路径 
        info = os.path.join(domain,name) #将路径与文件名结合起来就是每个文件的完整路径 
        data = pd.read_csv(info) #读取csv数据文件
        right_turn_signals = data[data['right_turn_signals'].isin([0])]
        left_turn_signals = data[data['left_turn_signals'].isin([0])]
        hand_brake = data[data['hand_brake'].isin([0])]
        foot_brake = data[data['foot_brake'].isin([0])]
        device_num = data['device_num']
        if len(right_turn_signals) ==len(device_num):
            print('{}的right_turn_signals中没有非0项''\n'.format(name))
            log_writter.write(str('{}的right_turn_signals中没有非0项''\n'.format(name)))
        else:
            print('{}的right_turn_signals中含有非0项''\n'.format(name))
            log_writter.write(str('{}的right_turn_signals中含有非0项''\n'.format(name)))
        if len(left_turn_signals) ==len(device_num):
            print('{}的left_turn_signals中没有非0项''\n'.format(name))
            log_writter.write(str('{}的left_turn_signals中没有非0项''\n'.format(name)))
        else:
            print('{}的left_turn_signals中含有有非0项''\n'.format(name))
            log_writter.write(str('{}的left_turn_signals中含有有非0项''\n'.format(name)))
        if len(hand_brake) ==len(device_num):
            print('{}的hand_brake中没有非0项''\n'.format(name))
            log_writter.write(str('{}的hand_brake中没有非0项''\n'.format(name)))
        else:
            print('{}的hand_brake中含有非0项''\n'.format(name))
            log_writter.write(str('{}的hand_brake中含有非0项''\n'.format(name)))
        if len(foot_brake) ==len(device_num):
            print('{}的foot_brake中没有非0项''\n'.format(name))
            log_writter.write(str('{}的foot_brake中没有非0项''\n'.format(name)))
        else:
            print('{}的foot_brake中含有非0项''\n'.format(name))
            log_writter.write(str('{}的foot_brake中含有非0项''\n'.format(name)))

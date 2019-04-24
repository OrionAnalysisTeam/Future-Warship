# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 08:47:56 2019

@author: 77
"""

import pandas as pd
import numpy as np
import os

for name in os.listdir('D:/the_data/new_data_tidu'): 
    domain = os.path.abspath(r'D:/the_data/new_data_tidu') #获取文件夹的路径 
    info = os.path.join(domain,name) #将路径与文件名结合起来就是每个文件的完整路径 
    data = pd.read_csv(info) #读取csv数据文件
    data =data[~data['delta_jingdu'].isin([0])]
    print('已过滤经度差为0的值')
    data =data[~data['delta_weidu'].isin([0])]
    print('已过滤纬度差为0的值')
    delta_jingdu = data['delta_jingdu'].copy()
    delta_weidu = data['delta_weidu'].copy()

    tidu_abs = np.abs(delta_weidu/delta_jingdu)
    print('已将梯度绝对值加入列表')
    tidu_abs = {'newtidu_abs':tidu_abs}
    newtidu_abs = pd.DataFrame(tidu_abs)
    the_mean = float(np.mean(newtidu_abs))
    print('已求出梯度平均值的绝对值')
    #定义绝对值为浮点数
    '''
    mean = []
    for i in range(0,len(tidu_abs)):
        if i > len(tidu_abs):
            break
        else:
            mean.append(the_mean)
    '''    
    
    our_data = pd.concat([data,newtidu_abs],axis=1) #将表格加入绝对值
    # our_data = our_data.drop(our_data.tidu_abs >(2*the_mean))
    #our_data = our_data.drop(['Unnamed: 0'], axis=1)
    our_data =  our_data.fillna(0)
    our_weidu = list(our_data['lat'].copy())
    our_jingdu = list(our_data['lng'].copy())
    atidu_abs = list(our_data['newtidu_abs'].copy())
    direction_angle=list(our_data['direction_angle'].copy())
    acc_state = list(our_data['acc_state'].copy())
    location_time = list(our_data['location_time'].copy())
    gps_speed = list(our_data['gps_speed'].copy())
    mileage = list(our_data['mileage'].copy())
    aframe = {'lat':our_weidu,'lng':our_jingdu,'atidu_abs':atidu_abs,'direction_angle':direction_angle,'acc_state':acc_state,'location_time':location_time,'gps_speed':gps_speed,'mileage':mileage}
    anew_data = pd.DataFrame(aframe)
    print('已建立新表格')
    anew_data = anew_data[anew_data['atidu_abs']<(2*the_mean)]
    print('已经排除大于2倍均值的行')
    anew_data = anew_data[anew_data['atidu_abs']>[0.2]]
    print('已经排除小于0.2的行')
    '''
    for i,u in zip(list(anew_data['atidu_abs'].copy()) ,range(0,len(anew_data['atidu_abs']))):  #遍历梯度和序号
        if i >= 2*the_mean:  #删除大于2
            anew_data = anew_data.drop(u)
            print('正在删除大于阈值')
        elif i <= 0.2:    #删除小于0.2
            anew_data = anew_data.drop(u)
            print('正在删除小于阈值')
        else:
            continue
    '''
    print('已完成数据清洗，准备输出')
    file_name = str('D:/the_data/our_new_data_tidu/{}'.format(name)) #设置文件及路径名
    anew_data.to_csv(file_name) #输出

    '''
    new_data.drop(np.abs(new_data['tidu_abs'])>np.abs(2*the_mean)
    '''
    
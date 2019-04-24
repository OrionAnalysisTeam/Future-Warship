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

for name in os.listdir('D:/the_data/the_data_tianjia'): 
    domain = os.path.abspath(r'D:/the_data/the_data_tianjia') #获取文件夹的路径 
    info = os.path.join(domain,name) #将路径与文件名结合起来就是每个文件的完整路径 
    data = pd.read_csv(info) #读取csv数据文件
    print('开始处理文件{}'.format(name))
    
    alist = []
    print('正在处理加速度')
    for i in range(1,len(data['gps_speed'])):
        jiasudu = (data['gps_speed'][i]-data['gps_speed'][i-1])/3.6
        alist.append(jiasudu)
    print('已求出文件{}的全部加速度'.format(name))
    jiasudu={'jiasudu':alist}
    jiasudu = pd.DataFrame(jiasudu)
    adata = pd.concat([data,jiasudu],axis=1)
    print('将加速度并入数据表格')
    
    blist = []
    print('正在处理转向角差')
    for j in range(1,len(adata['direction_angle'])):
        delta_zxj = adata['direction_angle'][j]-adata['direction_angle'][j-1]
        blist.append(delta_zxj)
    print('已求出文件{}的转向角差值'.format(name))
    delta_zxj={'delta_zxj':blist}
    delta_zxj = pd.DataFrame(delta_zxj)
    bdata = pd.concat([adata,delta_zxj],axis=1)
    print('已将转向角差值并入数据表格')
    
    print('正在处理梯度')
    bdata =bdata[~((data['delta_jingdu'].isin([0]))&(data['gps_speed']!=0))]  #加入速度条件后的
    print('已过滤经度差为0且速度不为0的值')
    '''
    data =data[~(data['delta_weidu'].isin([0]))&(data['gps_speed']!=0)]  #加入速度条件后的
    print('已过滤纬度差为0且速度不为0的值')
    '''
    delta_jingdu = bdata['delta_jingdu'].copy()
    delta_weidu = bdata['delta_weidu'].copy()

    tidu_abs = np.abs(delta_weidu/delta_jingdu)
    print('已求出梯度平均值的绝对值')
    tidu_abs = {'newtidu_abs':tidu_abs}
    newtidu_abs = pd.DataFrame(tidu_abs)
    the_mean = float(np.mean(newtidu_abs))
    print('已将梯度绝对值加入列表')
    #定义绝对值为浮点数
    '''
    mean = []
    for i in range(0,len(tidu_abs)):
        if i > len(tidu_abs):
            break
        else:
            mean.append(the_mean)
    '''    
    
    our_data = pd.concat([bdata,newtidu_abs],axis=1) #将表格加入绝对值
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
    jiasudu = list(our_data['jiasudu']).copy()
    delta_zxj = list(our_data['delta_zxj']).copy()
    aframe = {'lat':our_weidu,
              'lng':our_jingdu,
              'tidu_abs':atidu_abs,
              'direction_angle':direction_angle,
              'acc_state':acc_state,
              'location_time':location_time,
              'gps_speed':gps_speed,
              'mileage':mileage,
              'jiasudu':jiasudu,
              'delta_zxj':delta_zxj}
    anew_data = pd.DataFrame(aframe)
    print('已建立新表格') 
    anew_data.fillna(0)
    print('已用0填充空值')
    all_file = str('D:/the_data/best_data_A/{}'.format(name))
    anew_data.to_csv(all_file)
    print('已完成输出全新数据表格')
    
    print('正在开始清洗数据')
    anew_data = anew_data[anew_data['atidu_abs']<(2*the_mean)]
    print('已经排除大于2倍均值的行')
    anew_data = anew_data[~((anew_data['atidu_abs']<0.2)&(anew_data['gps_speed']!=0))]
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
    file_name = str('D:/the_data/best_data_B/{}'.format(name)) #设置文件及路径名
    anew_data.to_csv(file_name) #输出
    print('已完成输出清洗后的文件：{}'.format(name))

    '''
    new_data.drop(np.abs(new_data['tidu_abs'])>np.abs(2*the_mean)
    '''
print('数据处理工作已全部完成！')
    
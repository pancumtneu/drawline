#encoding: utf-8
import csv
import pandas as pd
import numpy as np
from mpl_toolkits.axisartist.axislines import SubplotZero
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
with open(r"eval_reward.csv") as c:
    r = csv.reader(c)
    step,train_error = [],[]
    index = 0
    for i in  r :
        if(index !=  0 ):
            step.append(i[1])
            train_error.append(i[2])

        #print(i)
        index =index+1
    list = ['step','train_error']
    lists = {};
    lists["step"],lists["train_error"],lists["validation_error"]= step,train_error,validation_error

x=range(0,800,2)
#plt.ylim(0,0.4)
line2,=plt.plot(x,train_error,'r--',linewidth=0.8)

ll=plt.legend([line3,line2],["validation_error","train_error"],loc='upper right')
'''
ax1 = plt.gca()
ax1.spines['top'].set_visible(False)  #去掉上边框
ax1.spines['right'].set_visible(False) #去掉右边框
'''
plt.grid(axis="y",linestyle='--')            #b, which, axis, color, linestyle, linewidth， **kwargs
plt.text(60000,0.13,'validation_error ',fontdict={'size': 9, 'color':  'blue'})       #字体尺寸9，颜色 蓝色   第一和第二个参数60000,0.13表示输出信息的坐标，原点坐标是（0，0）
plt.text(70000,-0.03,'train_error ',fontdict={'size': 9, 'color':  'red'})
plt.ylabel("error(%)",fontsize=11)     #设置纵轴单位
plt.xlabel("step",fontsize=11)         #设置横轴单位
#plt.title(" ",fontsize=11)            #设置图片的头部
plt.savefig('…/1.jpg',dpi=1200)       #图片保存位置，图片像素
plt.rcParams['figure.dpi'] =900        #分辨率
plt.show()

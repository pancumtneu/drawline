import csv
import numpy as np
from datetime import datetime
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
#filename=r"eval_reward.csv"
filename=r"ddpgresult.csv"



shortQvalue=[]

with open(filename,'r')as file:
    #1.创建阅读器对象
    reader=csv.reader(file)
    #2.读取文件头信息
    header_row=next(reader)

    #3.保存最高气温数据
    steps,Qvalue=[],[]
    for row in reader:
        #current_date=datetime.strptime(row[0],"%Y-%m-%d")
        steps.append(row[1])
        #4.将字符串转换为整型数据
        Qvalue.append((row[2]))
        Qvalue = list(map(float, Qvalue))
    Qvalue = [i + 300.0   for i in Qvalue]



    for i in range(len(Qvalue)):
        shortQvalue.append(round(float(Qvalue[i]),2))


    fig=plt.figure(dpi=512,figsize=(10,6))


    plt.xticks(rotation=30)  # 这里是调节横坐标的倾斜度，rotation是度数

    #6.将列表hights传个plot()方法
    plt.plot(steps,shortQvalue,c='red')
    #plt.hlines(0,0,8)

    #7.设置图形的格式
    # plt.title('Qvalue',fontsize=18)
    # for j in range(len(steps)):
    #     if j%100==0:
    #         plt.xticks([0,j])
    # xais=[]
    # for for j in max(steps)
    i_steps = list(map(int,steps))

    xais = []
    for j in range(max(i_steps)):
        if j%500==0:
            k=j/100
            xais.append(k)

    print(xais)
    plt.xticks(xais, rotation=20)
    plt.xlabel('step',fontsize=10)
    # # 8.绘制斜线日期标签
    # #fig.autofmt_xdate()
    plt.ylabel('eval_reward',fontsize=16)
    # plt.tick_params(axis='both',which='major',labelsize=16)
    plt.savefig('1.png', dpi=500)
    plt.show()


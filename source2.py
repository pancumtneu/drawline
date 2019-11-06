import csv  # 导入模块

milliseconds = []  # 创建用于存储时间的列表（横坐标）
amplitude = []  # 创建用于存储振幅的列表（纵坐标）

with open(r"eval_reward.csv") as f:  # 绝对路径，以‘r’模式处理（默认）
    dataReader = csv.reader(f)
    for row in dataReader:
        if (True):  # 索引为2的数据代表频率，因为发现15.多的是传递信息的。字符串切片转整型进行判断
            milliseconds.append(round(float(row[0])))  # 横坐标添加
            amplitude.append(float(row[1][1:]))  # 纵坐标添加

from matplotlib import pyplot as plt  # 导入模块

plt.plot(milliseconds, amplitude)  # 把横纵坐标对应的内容加进来
plt.show()  # 显示图窗
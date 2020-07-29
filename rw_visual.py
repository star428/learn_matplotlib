'''
@Author: your name
@Date: 2020-07-28 16:52:23  
@LastEditTime: 2020-07-29 09:53:00
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \learn_matplotlib\rw_visual.py
'''
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 只要处于活动状态，就不断的模拟随机漫步
while True:

    # 创建一个random walk实例同时把点都绘制出来
    rw = RandomWalk()
    rw.fill_walk()

    point_number = list(range(rw.number_points))
    # plt.scatter(rw.x_values,
    #            rw.y_values,
    #            c=point_number,
    #            cmap=plt.cm.Blues,
    #            s=1)
    plt.plot(rw.x_values, rw.y_values, linewidth=1)

    plt.scatter(rw.x_values[0], rw.y_values[0], c='green', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()
    keep_running = input("Do you want to continue?[y/n]:")
    if keep_running == 'n':
        break
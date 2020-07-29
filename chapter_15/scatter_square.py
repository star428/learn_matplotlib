'''
@Author: your name
@Date: 2020-07-28 14:59:21
@LastEditTime: 2020-07-28 15:39:56
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \learn_matplotlib\scatter_square.py
'''

import matplotlib.pyplot as plt


x_value = list(range(1, 1001))
y_value = [x**2 for x in x_value]

plt.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Blues,
            edgecolors='none', s=4)

# 设置图表标题同时给坐标轴加上标签
plt.title("Square numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of the Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)
# error labelsize

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

plt.show()

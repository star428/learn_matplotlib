'''
@Author: star428
@Date: 2020-07-27 21:57:46
@LastEditTime: 2020-07-28 11:05:40
@LastEditors: Please set LastEditors
@Description: test matplotlib
@FilePath: \learn_matplotlib\mpl_squares.py
'''

import matplotlib.pyplot as plt

input_value = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_value, squares, linewidth = 2)

# 设置图标标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("value", fontsize = 14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

plt.show()
'''
@Author: your name
@Date: 2020-07-28 15:46:16
@LastEditTime: 2020-07-28 15:59:20
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \learn_matplotlib\scatter_cube.py
'''


import matplotlib.pyplot as plt


x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.PuRd, s=4)

plt.title("Cube numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of value", fontsize=14)

plt.tick_params(axis='both', labelsize=14)

plt.axis([0, 5000, 0, 5000**3])

plt.show()
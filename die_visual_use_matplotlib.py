'''
@Author: your name
@Date: 2020-07-29 15:40:13
@LastEditTime: 2020-07-29 16:46:45
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \learn_matplotlib\die_visual_use_matplotlib.py
'''
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from die import Die

die = Die()
results = [die.roll() for roll_number in range(1000)]

frequencies = [
    results.count(value) for value in range(1, die.number_sides + 1)
]

labels = list(range(1, die.number_sides + 1))
# men_means = [20, 34, 30, 35, 27]
# women_means = [25, 32, 34, 20, 25]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x, frequencies, width, label='Result', color='blueviolet')
# rects2 = ax.bar(x + width / 2, results, width, label='Women')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Frequency of Results')
ax.set_title('Result of rolling one D6 1000 times')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate(
            '{}'.format(height),
            xy=(rect.get_x() + rect.get_width() / 2, height),
            xytext=(0, 3),  # 3 points vertical offset
            textcoords="offset points",
            ha='center',
            va='bottom')


autolabel(rects1)
# autolabel(rects2)

fig.tight_layout()

plt.show()
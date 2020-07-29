'''
@Author: your name
@Date: 2020-07-29 10:56:10
@LastEditTime: 2020-07-29 11:26:55
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \learn_matplotlib\die_visual.py
'''
import pygal

from die import Die

die = Die()

# 掷几次骰子同时把结果保存在results中
results = []

for roll_number in range(1000):
    result = die.roll()
    results.append(result)

frequencies = []

for value in range(1, die.number_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
line_chart = pygal.Bar()

line_chart.title = "Result of rolling one D6 1000 times"
line_chart.x_labels = list(range(1, 7))
line_chart.x_title = "Result"
line_chart.y_title = "Frequency of Results"

line_chart.add("D6", frequencies)
line_chart.render_to_file('die_visual.svg')

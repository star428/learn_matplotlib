'''
@Author: your name
@Date: 2020-07-29 14:25:02
@LastEditTime: 2020-07-29 14:34:47
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \learn_matplotlib\dice_visual.py
'''
import pygal

from die import Die

die_1 = Die()
die_2 = Die()

# 掷几次骰子同时把结果保存在results中
results = []

for roll_number in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []

max_result = die_1.number_sides + die_2.number_sides

for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
line_chart = pygal.Bar()

line_chart.title = "Result of rolling two D6 1000 times"
line_chart.x_labels = list(range(2, max_result + 1))  # 设置2~12的x标签
line_chart.x_title = "Result"
line_chart.y_title = "Frequency of Results"

line_chart.add("D6 + D6", frequencies)
line_chart.render_to_file('dice_visual.svg')

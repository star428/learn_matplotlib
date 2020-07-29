'''
@Author: your name
@Date: 2020-07-29 14:37:26
@LastEditTime: 2020-07-29 14:46:17
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \learn_matplotlib\different_dice.py
'''
import pygal

from die import Die

die_1 = Die(6)
die_2 = Die(10)

# 掷几次骰子同时把结果保存在results中
results = [die_1.roll() + die_2.roll() for roll_number in range(5000)]

# for roll_number in range(5000):
#     result = die_1.roll() + die_2.roll()
#     results.append(result)

max_result = die_1.number_sides + die_2.number_sides

frequencies = [results.count(value) for value in range(2, max_result + 1)]

# for value in range(2, max_result + 1):
#     frequency = results.count(value)
#     frequencies.append(frequency)

# 对结果进行可视化
line_chart = pygal.Bar()

line_chart.title = "Result of rolling D6 and D10 1000 times"
line_chart.x_labels = list(range(2, max_result + 1))  # 设置2~12的x标签
line_chart.x_title = "Result"
line_chart.y_title = "Frequency of Results"

line_chart.add("D6 + D10", frequencies)
line_chart.render_to_file('dice_D6_ad_D10_visual.svg')

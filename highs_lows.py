'''
@Author: your name
@Date: 2020-07-30 08:49:15
@LastEditTime: 2020-07-30 11:17:32
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \learn_matplotlib\highs_lows.py
'''
import csv
from datetime import datetime
import matplotlib.pyplot as plt

import functions_for_weather as fc
# filename = 'sitka_weather_07-2014.csv'
filename_sitka = 'sitka_weather_2014.csv'
filename_death_valley = 'death_valley_2014.csv'

# 画底层同时画线
fig = plt.figure(dpi=128, figsize=(10, 7))
datas, highs, lows = fc.analyze_temoeratures(filename_death_valley)
fc.plot_highs_lows(datas, highs, lows, middle_color='darkorange')

datas, highs, lows = fc.analyze_temoeratures(filename_sitka)
fc.plot_highs_lows(datas,
                   highs,
                   lows,
                   highs_color='lightcoral',
                   lows_color='aqua',
                   middle_color='green')
# 设置标签等
plt.title("Daily high and low temperatures - 2014", fontsize=24)
plt.xlabel('', fontsize=16)
# 使x轴上的标签倾斜
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.ylim([0, 120])
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
'''
@Author: your name
@Date: 2020-07-30 11:08:09
@LastEditTime: 2020-07-30 11:17:56
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \learn_matplotlib\functions_for_weather.py
'''
import csv
from datetime import datetime
import matplotlib.pyplot as plt


def analyze_temoeratures(filename):
    """[分析天气数据表格返回日期list，最高气温list，最低气温list]

    Args:
        filename ([csv]): [文件名]

    Returns:
        datas：日期list
        highs：最高气温list
        lows：最低气温list
    """
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        header_row = next(reader)
        # print(header_row)

        # for index, column_header in enumerate(header_row):
        #     print(index, column_header)
        datas = []
        highs = []
        lows = []
        for row in reader:
            try:
                current_data = datetime.strptime(row[0], r"%Y-%m-%d")
                high = int(row[1])
                low = int(row[3])
            except ValueError:
                print(current_data, "lost the data.")
            else:
                datas.append(current_data)
                highs.append(high)
                lows.append(low)
        return datas, highs, lows
    # for row in reader:
    #     highs.append(int(row[1]))


def plot_highs_lows(datas,
                    highs,
                    lows,
                    highs_color='red',
                    lows_color='blue',
                    middle_color='blue'):
    """画出最高温度曲线和最低温度曲线同时在其中填充

    Args:
        datas ([list]): [日期]
        highs ([list]): [最高温度]
        lows ([list]): [最低温度]
        颜色类：
        分别代表上下和中间的填充颜色
    """
    plt.plot(datas, highs, c=highs_color)
    plt.plot(datas, lows, c=lows_color)
    plt.fill_between(datas, highs, lows, facecolor=middle_color, alpha=0.3)
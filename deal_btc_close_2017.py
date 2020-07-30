'''
@Author: your name
@Date: 2020-07-30 15:12:24
@LastEditTime: 2020-07-30 20:25:16
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \learn_matplotlib\deal_btc_close_2017.py
'''
import json
import pygal
import math
from itertools import groupby

# 将数据加载到一个列表中
filename = 'btc_close_2017_request.json'
with open(filename) as f:
    btc_data = json.load(f)
# 打印每一天的消息
# for btc_dict in btc_data:
#     print("{} is mouth {} week {}, {}, the close price is {} RMB.".format(
#         btc_dict['date'],
#         btc_dict['month'],
#         btc_dict['week'],
#         btc_dict['weekday'],
#         btc_dict['close'],
#     ))
date = []
month = []
week = []
weekday = []
close = []
for btc_dict in btc_data:
    date.append(btc_dict['date'])
    month.append(int(btc_dict['month']))
    week.append(int(btc_dict['week']))
    weekday.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))
# 将数值做对数变换
close_log = [math.log10(num) for num in close]
# 绘图部分
line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = "收盘价对数变换（￥）"
line_chart.x_labels = date
N = 20  # x轴坐标每隔20天显示一次
line_chart.x_labels_major = date[::N]  # 也就是切片步长
line_chart.add('log收盘价', close_log)
line_chart.render_to_file("收盘价对数变换折线图（￥）.svg")


def draw_line(x_data, y_data, title, y_legend):
    xy_map = []
    for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]):
        y_list = [v for _, v in y]
        xy_map.append([x, sum(y_list) / len(y_list)])
    x_unique, y_mean = [*zip(*xy_map)]
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    line_chart.render_to_file(title + '.svg')
    return line_chart


# 月 日均值
idx_month = date.index('2017-12-01')
line_chart_month = draw_line(month[:idx_month], close[:idx_month],
                             '收盘价月日均值（￥）', '月日均值')
# 周 日均值
idx_week = date.index('2017-12-11')
line_chart_week = draw_line(week[1:idx_week], close[1:idx_week], '收盘价周日均值（￥）',
                            '周日均值')
# 星期 日均值
wd = [
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
    'Sunday'
]
weekday_int = [wd.index(w) + 1 for w in weekday[1:idx_week]]
line_chart_weekday = draw_line(weekday_int, close[1:idx_week], "收盘价星期均值（￥）",
                               "星期均值")
line_chart_weekday.x_labels = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
line_chart_weekday.render_to_file('收盘价星期均值（￥）.svg')

with open('收盘价Dashboard.html', 'w', encoding='utf8') as html_file:
    html_file.write(
        '<html><head><title>收盘价Dashboard</title><metacharset="utf-8></head><body>\n'
    )
    for svg in [
            '收盘价周日均值（￥）.svg', '收盘价对数变换折线图（￥）.svg', '收盘价折线图（￥）.svg',
            '收盘价星期均值（￥）.svg', '收盘价月日均值（￥）.svg'
    ]:
        html_file.write(
            '   <object type="image/svg+xml" data="{0}" height=500></object>\n'
            .format(svg))
    html_file.write('</body></html>')
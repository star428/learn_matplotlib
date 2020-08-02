'''
@Author: your name
@Date: 2020-08-01 17:11:34
@LastEditTime: 2020-08-02 10:39:03
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \learn_matplotlib\hn_submissions.py
'''
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
import requests
from operator import itemgetter

# 执行API调用并存储相应
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)

# 处理关于每篇文章的信息
submission_ids = r.json()  # 返回的是一个list,其中包括所有的id
titles, submission_dicts = [], []
for submission_id in submission_ids[:30]:
    # 对于每篇文章，都执行一个API调用
    url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) +
           '.json')
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()  # 返回的是一个字典，包含很多信息

    submission_dict = {
        'value': int(response_dict.get('descendants', 0)),
        'xlink': 'http://news.ycombinator.com/item?id=' + str(submission_id),
    }
    # test
    # print(submission_dict['comments'])
    # test
    titles.append(response_dict['title'])
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts,
                          key=itemgetter('value'),
                          reverse=True)

# test
# print(submission_dicts[0]['comments'])
# test
# 绘图部分

my_style = LS('#333366', base_style=LCS)
# 设置pygal样式
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

line_chart = pygal.Bar(my_config, style=my_style)
line_chart.title = 'Hn_Submissions'
line_chart.x_labels = map(str, titles)
line_chart.add('', submission_dicts)

line_chart.render_to_file('hn_dubmissions.svg')

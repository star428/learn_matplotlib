'''
@Author: your name
@Date: 2020-07-31 09:55:45
@LastEditTime: 2020-08-02 10:54:25
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \learn_matplotlib\python_repo.py
'''
import pygal
import requests
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('status code:', r.status_code)
response_dict = r.json()
# print("total repositories:", response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']
# print('Repositories returned:', len(repo_dicts))

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': str(repo_dict['description']),
        'xlink':repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)

name_list = [
    'Name: ', 'Owner: ', 'Stars: ', 'Repository: ', 'Created: ', 'Updated: ',
    'Description: '
]
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
line_chart.title = 'Most-Starred Python Projects On Github'
line_chart.x_labels = map(str, names)
line_chart.add('', plot_dicts)

line_chart.render_to_file('Python_repo.svg')

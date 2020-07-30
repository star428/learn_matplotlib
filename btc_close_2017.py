'''
@Author: your name
@Date: 2020-07-30 14:55:48
@LastEditTime: 2020-07-30 15:06:13
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \learn_matplotlib\btc_close_2017.py
'''
import requests

json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
req = requests.get(json_url)
# 将数据写入文件
with open('btc_close_2017_request.json', 'w') as f:
    f.write(req.text)
file_requests = req.json()
'''
@Author: your name
@Date: 2020-08-02 10:54:49
@LastEditTime: 2020-08-02 11:08:07
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \learn_matplotlib\test_python_repos.py
'''
import unittest
import requests


class TestStats(unittest.TestCase):
    """测试status能否输出200"""
    def test_status_code(self):
        url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
        r = requests.get(url)
        self.assertEqual(r.status_code, 200)

    def test_deskep(self):
        url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
        r = requests.get(url)
        # print('status code:', r.status_code)
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
                'xlink': repo_dict['html_url']
            }
            plot_dicts.append(plot_dict)
        self.assertLess(len(plot_dicts), 40)


unittest.main()
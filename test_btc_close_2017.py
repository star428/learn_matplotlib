'''
@Author: your name
@Date: 2020-07-30 20:02:26
@LastEditTime: 2020-07-30 20:41:00
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \learn_matplotlib\test_btc_close_2017.py
'''
import unittest
import pygal
from deal_btc_close_2017 import draw_line


class DrawTest(unittest.TestCase):
    """测试方法draw_line"""
    def test_draw_line(self):
        x_test = [1, 1, 1, 2, 2, 2, 3, 3, 3]
        y_test = [1, 1, 1, 2, 2, 2, 3, 3, 3]
        test_line_chart = draw_line(x_test, y_test, 'Test title', 'Test_y')
        self.assertEqual(test_line_chart.x_labels, [1, 2, 3])
        self.assertEqual(test_line_chart.title, 'Test title')


unittest.main()
'''
@Author: your name
@Date: 2020-07-29 10:28:46
@LastEditTime: 2020-07-29 10:55:38
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \learn_matplotlib\die.py
'''
from random import randint


class Die:
    """表示骰子的一个类"""
    def __init__(self, number_sides=6):
        '''默认骰子为六面'''
        self.number_sides = number_sides

    def roll(self):
        '''返回1到骰子面数的随机值'''
        return randint(1, self.number_sides)

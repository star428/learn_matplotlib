'''
@Author: your name
@Date: 2020-07-28 16:33:01
@LastEditTime: 2020-07-29 10:07:46
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \learn_matplotlib\random_walk.py
'''
from random import choice


class RandomWalk:
    def __init__(self, number_points=5000) -> None:
        """初始化随机漫步的属性"""
        self.number_points = number_points

        # 所有随机漫步都始于（0，0）
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机漫步包含的所有点"""

        # 不断漫步直到列表到达指定长度
        while len(self.x_values) < self.number_points:
            # 决定前进方向以及沿这个方向前进的距离
            x_step = get_step()
            y_step = get_step()

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x和y值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)


def get_step():
    """计算移动的方向和距离并返回"""
    direction = choice([-1, 1])
    distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
    return direction * distance

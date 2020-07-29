'''
@Author: your name
@Date: 2020-07-29 14:55:32
@LastEditTime: 2020-07-29 15:26:37
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \learn_matplotlib\rw_visual_use_pygal.py
'''
import pygal
from random_walk import RandomWalk

rw = RandomWalk(1000)
rw.fill_walk()

point_lists = make_tuple(rw.x_values, rw.y_values)

xy_chart = pygal.XY(stroke=False)
xy_chart.title = 'Correlation'
xy_chart.add('A', point_lists)

xy_chart.add('Start Point', [point_lists[0]])
xy_chart.add('End point', [point_lists[-1]])

xy_chart.render_to_file('rw_visual.svg')


def make_tuple(list_1, list_2):
    """[输入两个列表整合成（x,y）的形式的列表再输出]

    Args:
        list_1 ([list]): [description]
        list_2 ([list]): [description]

    Returns:
        [list]: [返回一个列表]
    """
    points_xy = [(list_1[point_number], list_2[point_number])
                 for point_number in range(len(list_1))]
    # for point_number in range(len(list_1)):
    #     your_tuple = (list_1[point_number], list_2[point_number])
    #     points_xy.append(your_tuple)

    return points_xy

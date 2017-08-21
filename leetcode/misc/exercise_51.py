# -*- coding: utf-8 -*-
"""
这里的这个问题是对八皇后问题的一个简单的扩展，将其扩展成了n皇后问题。
这个问题是对回溯法的一个检验，因为我们知道题目中要求将所有的解决方案
都找到。
回溯法的三个要素：确定解空间，解空间结构，以及深度优先搜索。

这个问题中有一个核心的问题就是判断解的合理性。

"""
from __future__ import print_function


def generate_children(state):
    """
    根据棋盘的状态生成下一个可以放置“皇后”的位置
    """
    len_state = len(state)
    children = []
    for i in range(len_state):
        for j in range(len_state):
            if state[i][j] > 0:
                continue
            else:
                children.append((i, j))
    return children


def update_board_state(state, x, y, plus=True):
    """
    更新棋盘的状态
    """
    unit = 1 if plus else -1
    length = len(state)
    # 更新十字交叉位置的棋盘状态
    for i in range(length):
        state[i][y] += unit
        state[x][i] += unit
    # 更新X交叉位置的棋盘状态
    for i in range(4):
        start_x, start_y = x, y
        x_flag = i / 2
        y_flag = i % 2
        x_step, y_step = pow(-1, x_flag), pow(-1, y_flag)
        while (0 <= start_x < length) and (0 <= start_y < length):
            state[start_x][start_y] += unit
            start_x += x_step
            start_y += y_step


class Node(object):

    def __init__(self, parent, board_state):
        self.parent = parent
        self.board_state = board_state
        self.length = len(board_state)
        self.children = generate_children(board_state)

    def empty(self):
        return False if self.children else True

    def next(self):
        x, y = self.children.pop()
        update_board_state(self.board_state, x, y)
        return self.board_state

class Solution(object):

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # 初始化棋盘状态，每一个位置的数字代表该位置被多少个“皇后”访问到
        initial_state = [[0] * n for _ in range(n)]
        root = Node(None, initial_state)
        temp_node = root
        while temp_node:
            if temp_node.empty():
                
                pass
            else:
                pass
            pass
        pass

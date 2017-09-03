# -*- coding: utf-8 -*-
"""
这里的这个问题是对八皇后问题的一个简单的扩展，将其扩展成了n皇后问题。
这个问题是对回溯法的一个检验，因为我们知道题目中要求将所有的解决方案
都找到。
回溯法的三个要素：确定解空间，解空间结构，以及深度优先搜索。

这个问题中有一个核心的问题就是判断解的合理性。

"""
from __future__ import print_function


class Node(object):

    def __init__(self, x, y, parent, positions, level):
        self.x = x
        self.y = y
        self.parent = parent
        self.positions = positions
        self.level = level
        self.idx = 0

    def empty(self):
        return False if self.positions else True

    def next(self):
        x, y = self.positions[self.idx]
        self.idx += 1
        children = []
        for temp_x, temp_y in self.positions:
            if temp_x == x or temp_y == y:
                continue
            if abs((temp_y - y) / (temp_x - x)) == 1:
                continue
            children.append((temp_x, temp_y))
        return (x, y), children


class Solution(object):

    def generate_solution(self, tree_node):
        solution = []
        while tree_node:
            solution.append((tree_node.x, tree_node.y))
            tree_node = tree_node.parent
        return solution

    def solveNQueens(self, n):
        """
        对于这个
        :type n: int
        :rtype: List[List[str]]
        """
        positions = []
        for i in range(n):
            for j in range(n):
                positions.append((i, j))
        root = Node(None, positions, 0)
        temp_node = root
        solutions = []
        while temp_node:
            if temp_node.level == n:
                solutions.append(self.generate_solution(temp_node))
                temp_node = temp_node.parent
                continue
            if not temp_node.positions:
                temp_node = temp_node.parent
            else:
                (next_x, next_y), children = temp_node.next()
                temp_node = Node(temp_node, children, temp_node.level + 1)
        pass

class ChessBoard(object):
    """
    棋盘状态类对象
    """

    def __init__(self, width):
        """
        :type width: int
            棋盘的宽度大小
        """
        self.width = width
        self.placed_chess = []
        self.next_x = 0
        self.next_y = 0

    def _next_position(self):
        """
        移动到棋盘的下一个位置
        """
        self.next_x += 1
        if self.next_x == self.width:
            self.next_x %= self.width
            self.next_y += 1
            if self.next_y == self.width
                return False
        return True

    def place_next_chess(self):
        x, y = self.next_x, self.next_y

        pass

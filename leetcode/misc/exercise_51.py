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
        """
        :type x: int
            生成该结点的x坐标
        :type y: int
            生成该结点的y坐标
        :type parent: Node
            生成该结点的双亲结点的引用
        :type positions: List
            该结点可以使用的有效位置元组的列表
        :type level: int
            记录该结点在树中的高度，代表已经在棋盘上放置的棋子的数目
        """
        self.x = x
        self.y = y
        self.have_children = False
        self.parent = parent
        self.positions = positions
        self.level = level
        if self.positions:
            self.have_children = True

    def empty(self):
        """
        返回时候该结点还存在可以用来生成孩子结点的有效位置
        """
        return not self.have_children

    def next(self):
        """
        生成下一个用于生成孩子结点的位置以及有效的放置棋子的位置
        """
        x, y = self.positions.pop()
        if len(self.positions) == 0:
            self.have_children = False

        children = []
        for temp_x, temp_y in self.positions:
            if temp_x == x or temp_y == y:
                continue
            if abs(abs((temp_y - y) * 1.0 / (temp_x - x)) - 1) < 0.0001:
                continue
            children.append((temp_x, temp_y))
        return (x, y), children


class Solution(object):

    def generate_solution(self, tree_node):
        """
        根据一个搜索树的叶子结点生成一个解法的放置棋子的位置元组列表
        """
        solution = []
        while tree_node.parent:
            solution.append((tree_node.x, tree_node.y))
            tree_node = tree_node.parent
        return solution

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # 根结点可以放置的位置是整个棋盘上的所有位置
        positions = []
        for i in range(n):
            for j in range(n):
                positions.append((i, j))
        # 生成树的根结点
        root = Node(None, None, None, positions, 0)
        temp_node = root
        solutions = []
        while temp_node:
            if temp_node.level == n:  # 说明n个位置都已经放置棋子，则返回结果
                solutions.append(self.generate_solution(temp_node))
                temp_node = temp_node.parent
                continue
            if temp_node.empty():  # 代表该结点不能再生成子结点
                temp_node = temp_node.parent
            else:  # 代表该结点还可以生成子结点
                (next_x, next_y), children = temp_node.next()
                temp_node = Node(next_x, next_y, temp_node, children, temp_node.level + 1)

        result = []
        for solution in solutions:
            chess_board = [['.'] * n for _ in range(n)]
            for x, y in solution:
                chess_board[x][y] = 'Q'
            chess_board = [''.join(item) for item in chess_board]
            result.append(chess_board)
        return result


s = Solution()
print(s.solveNQueens(8))

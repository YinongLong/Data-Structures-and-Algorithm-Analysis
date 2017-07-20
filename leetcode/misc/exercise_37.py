# -*- coding: utf-8 -*-
from __future__ import print_function

from collections import defaultdict

class Solution(object):

    def get_location_info(self, i, j):
        return ('r%d' % i, 'c%d' % j, 'b%d%d' % (i/3, j/3))

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        size = len(board)

        # 首先统计整个数独board的信息
        state = defaultdict(set)
        for i in range(size):
            row = board[i]
            for j in range(size):
                item = row[j]
                if item == '.':
                    continue
                for info in self.get_location_info(i, j):
                    state[item].add(info)

        # 然后利用统计的数独board的信息来进行填数
        i = j = 0
        locations = []
        while i < size:
            numbers = map(str, range(1, 10))
            temp_location = []
            while j < size:
                item = board[i][j]
                if item == '.':
                    temp_location.append((i, j))
                else:
                    numbers.remove(item)
                j += 1
            for location in temp_location:
                r_id, c_id, b_id = self.get_location_info(*location)
                for number in numbers:
                    states_space = state[number]
                    if (r_id not in states_space) and (c_id not in states_space) and (b_id not in states_space):
                        pass
                pass
            i += 1

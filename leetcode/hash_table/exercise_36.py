# -*- coding: utf-8 -*-
from __future__ import print_function

from collections import defaultdict

class Solution(object):

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        size = len(board)
        state = defaultdict(set)
        for i in range(size):
            row = board[i]
            for j in range(size):
                item = row[j]
                if item == '.':
                    continue
                row_id = 'r%d' % i
                col_id = 'c%d' % j
                box_id = 'b%d%d' % (i/3, j/3)
                if (row_id in state[item]) or (col_id in state[item]) or (box_id in state[item]):
                    return False
                else:
                    state[item].add(row_id)
                    state[item].add(col_id)
                    state[item].add(box_id)
        return True

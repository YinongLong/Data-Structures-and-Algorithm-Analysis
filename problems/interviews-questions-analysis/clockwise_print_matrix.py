# -*- coding: utf-8 -*-
from __future__ import print_function

class Solution(object):

    def printMatrix(self, matrix):
        num_row = len(matrix)
        if num_row == 0:
            return []
        num_col = len(matrix[0])
        if num_col == 0:
            return []

        low_row_bound = -1; high_row_bound = num_row
        left_col_bound = -1; right_col_bound = num_col
        start_p = [0, 0]
        result = []
        flag = 0
        while (high_row_bound > start_p[0] > low_row_bound) and \
            (right_col_bound > start_p[1] > left_col_bound):

            result.append(matrix[start_p[0]][start_p[1]])
            if flag == 0:  # col +
                start_p[1] += 1
                if start_p[1] == right_col_bound:
                    low_row_bound += 1
                    start_p[1] -= 1
                    start_p[0] += 1
                    flag = 1
            elif flag == 1:  # row +
                start_p[0] += 1
                if start_p[0] == high_row_bound:
                    right_col_bound -= 1
                    start_p[0] -= 1
                    start_p[1] -= 1
                    flag = 2
            elif flag == 2:  # col -
                start_p[1] -= 1
                if start_p[1] == left_col_bound:
                    high_row_bound -= 1
                    start_p[1] += 1
                    start_p[0] -= 1
                    flag = 3
            else:  # row -
                start_p[0] -= 1
                if start_p[0] == low_row_bound:
                    left_col_bound += 1
                    start_p[0] += 1
                    start_p[1] += 1
                    flag = 0
        return result

s = Solution()
print(s.printMatrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))

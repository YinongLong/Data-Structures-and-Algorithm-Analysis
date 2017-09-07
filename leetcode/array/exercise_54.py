# -*- coding: utf-8 -*-
from __future__ import print_function


class Spider(object):

    def __init__(self, state_matrix, width, height):
        self.state_matrix = state_matrix
        self.width = width
        self.height = height
        self.posi_x = 0
        self.posi_y = 0
        self.to_right = True
        self.to_down = False
        self.to_left = False
        self.to_up = False

    def next_position(self):
        while 1:
            if self.to_right:
                self.posi_y += 1
                if (self.posi_y >= self.width) or (self.state_matrix[self.posi_x][self.posi_y] is None):
                    self.posi_y -= 1
                    self.to_right = False
                    self.to_down = True
                else:
                    break
            if self.to_down:
                self.posi_x += 1
                if (self.posi_x >= self.height) or (self.state_matrix[self.posi_x][self.posi_y] is None):
                    self.posi_x -= 1
                    self.to_down = False
                    self.to_left = True
                else:
                    break
            if self.to_left:
                self.posi_y -= 1
                if (self.posi_y < 0) or (self.state_matrix[self.posi_x][self.posi_y] is None):
                    self.posi_y += 1
                    self.to_left = False
                    self.to_up = True
                else:
                    break
            if self.to_up:
                self.posi_x -= 1
                if (self.posi_x < 0) or (self.state_matrix[self.posi_x][self.posi_y] is None):
                    self.posi_x += 1
                    self.to_up = False
                    self.to_right = True
                else:
                    break
        result = self.state_matrix[self.posi_x][self.posi_y]
        self.state_matrix[self.posi_x][self.posi_y] = None
        return result

class Solution(object):

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        height = len(matrix)
        width = len(matrix[0])
        spider = Spider(matrix, width, height)
        result = []
        while len(result) < (width * height):
            temp_num = spider.next_position()
            print(temp_num)
            result.append(temp_num)
        return result


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
s = Solution()
print(s.spiralOrder(matrix))

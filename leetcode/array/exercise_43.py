# -*- coding: utf-8 -*-
from __future__ import print_function

class Solution(object):

    def addition(self, nums_list, idx, num):
        nums_list[idx] += num
        if nums_list[idx] >= 10:
            nums_list[idx] %= 10
            nums_list[idx-1] += 1

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = list(num1)
        num2 = list(num2)
        len_num1 = len(num1)
        len_num2 = len(num2)
        result = [0] * (len_num1 + 1 + len_num2 + 1 - 1)
        for i in range(-1, -len_num2 - 1, -1):
            temp_result = [0] * (len_num1 + 1)
            temp_num2 = int(num2[i])
            for j in range(-1, -len_num1 - 1, -1):
                temp_num1 = int(num1[j])
                product = temp_num1 * temp_num2
                self.addition(temp_result, j, product % 10)
                self.addition(temp_result, j-1, product / 10)
            for k in range(-1, -len(temp_result)-1, -1):
                self.addition(result, k + i + 1, temp_result[k])
        str_result = []
        starting = False
        for item in result:
            if starting:
                str_result.append(str(item))
            else:
                if item != 0:
                    starting = True
                    str_result.append(str(item))
        if str_result:
            return ''.join(str_result)
        else:
            return '0'


num1 = '758'
num2 = '234'
s = Solution()
print(s.multiply(num1, num2))

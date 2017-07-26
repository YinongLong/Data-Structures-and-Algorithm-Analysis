# -*- coding: utf-8 -*-
from __future__ import print_function

class Solution(object):

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = list(num1)
        num2 = list(num2)
        result = []
        for i in range(-1, -len(num2)-1, -1):
            temp_result = []
            location = None
            temp_num2 = int(num2[i])
            for j in range(-1, -len(num1)-1, -1):
                temp_num1 = int(num1[j])
                product = temp_num1 * temp_num2
                if location is None:
                    temp_result.append(product % 10)
                    
            pass
        pass

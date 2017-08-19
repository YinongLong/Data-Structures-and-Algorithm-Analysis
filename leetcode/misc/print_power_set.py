# -*- coding: utf-8 -*-
"""
print all combinations of a set. for example, there is an array {1, 2, 3}, its
power set is:
{#}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}
"""
from __future__ import print_function

class Solution(object):

    def binary_idea(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        len_nums = len(nums)
        total_nums = 1 << len_nums
        result = []
        for i in range(total_nums):
            result.append([])
            for j in range(len_nums):
                signal = 1 << j
                if signal & i:
                    result[-1].append(nums[j])
            if len(result[-1]) == 0:
                result[-1].append('#')
        return result


nums = [1, 2, 3]
s = Solution()
print(s.binary_idea(nums))

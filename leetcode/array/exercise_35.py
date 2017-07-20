# -*- coding: utf-8 -*-
from __future__ import print_function


class Solution(object):

    def binary_search(self, s_idx, e_idx, target, array):
        if s_idx <= e_idx:
            m_idx = (s_idx + e_idx) / 2
            if array[m_idx] == target:
                return m_idx
            elif array[m_idx] > target:
                return self.binary_search(s_idx, m_idx-1, target, array)
            else:
                return self.binary_search(m_idx+1, e_idx, target, array)
        else:
            return e_idx + 1

    def searchInsert(self, nums, target):
        """
        直接进行二分查找即可
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binary_search(0, len(nums)-1, target, nums)


numbers = [1, 3, 5, 6]
s = Solution()
print(s.searchInsert(numbers, 7))

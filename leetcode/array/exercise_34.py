# -*- coding: utf-8 -*-
from __future__ import print_function

class Solution(object):

    def binary_search(self, s_idx, e_idx, array, target):
        """
        :type s_idx: int
        :type e_idx: int
        :type array: List[int]
        :rtype: int
        """
        if s_idx <= e_idx:
            m_idx = (s_idx + e_idx) / 2
            if array[m_idx] == target:
                return m_idx
            elif array[m_idx] > target:
                return self.binary_search(s_idx, m_idx-1, array, target)
            else:
                return self.binary_search(m_idx+1, e_idx, array, target)
        else:
            return -1

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_len = len(nums)
        if nums_len == 0:
            return [-1, -1]
        m_idx = self.binary_search(0, nums_len-1, nums, target)
        if m_idx == -1:
            return [-1, -1]
        else:
            left_bound = m_idx
            temp_m = self.binary_search(0, m_idx-1, nums, target)
            while temp_m != -1:
                left_bound = temp_m
                temp_m = self.binary_search(0, temp_m-1, nums, target)
            right_bound = m_idx
            temp_m = self.binary_search(m_idx+1, nums_len-1, nums, target)
            while temp_m != -1:
                right_bound = temp_m
                temp_m = self.binary_search(temp_m+1, nums_len-1, nums, target)
            return [left_bound, right_bound]


numbers = [5, 7, 7, 8, 8, 10]
s = Solution()
print(s.searchRange(numbers, 8))

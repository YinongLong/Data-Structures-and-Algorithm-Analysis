# -*- coding: utf-8 -*-
from __future__ import print_function

class Solution(object):

    def find_maximum_subarray(self, s_idx, e_idx, array):
        """
        :type s_idx: int
        :type e_idx: int
        :type array: List[int]
        :rtype: int
        """
        if s_idx < e_idx:
            m_idx = (s_idx + e_idx) / 2
            left_max = self.find_maximum_subarray(s_idx, m_idx, array)
            right_max = self.find_maximum_subarray(m_idx+1, e_idx, array)
            temp_right_max = array[m_idx+1]
            temp_sum = 0
            for i in range(m_idx+1, e_idx+1):
                temp_sum += array[i]
                if temp_sum > temp_right_max:
                    temp_right_max = temp_sum
            temp_left_max = array[m_idx]
            temp_sum = 0
            for i in range(m_idx, s_idx-1, -1):
                temp_sum += array[i]
                if temp_sum > temp_left_max:
                    temp_left_max = temp_sum
            mid_max = temp_left_max + temp_right_max
            return max(left_max, mid_max, right_max)
        else:
            return array[s_idx]

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = self.find_maximum_subarray(0, len(nums)-1, nums)
        return maximum

    def maxSubArray_DP(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        assert len(nums) > 0
        nums_len = len(nums)
        state_array = dict()
        state_array[0] = nums[0]
        maximum = nums[0]
        for i in range(1, nums_len):
            addition = state_array[i-1] if state_array[i-1] > 0 else 0
            state_array[i] = addition + nums[i]
            maximum = maximum if maximum > state_array[i] else state_array[i]
        return maximum


numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
s = Solution()
print(s.maxSubArray_DP(numbers))

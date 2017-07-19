# -*- coding: utf-8 -*-
from __future__ import print_function

class Solution(object):

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        i = 0
        if target == nums[0]:
            return 0
        elif target == nums[-1]:
            return len(nums) - 1
        elif target > nums[0]:
            i += 1
            while i < len(nums):
                if nums[i] < nums[i-1]:
                    break
                if nums[i] == target:
                    return i
                i += 1
            return -1
        elif target < nums[-1]:
            i = -2
            while abs(i) <= len(nums):
                if nums[i+1] < nums[i]:
                    break
                if nums[i] == target:
                    return len(nums) + i
                i -= 1
            return -1
        else:
            return -1


numbers = [4, 5, 6, 7, 0, 1, 2]
s = Solution()
print(s.search(numbers, 0))

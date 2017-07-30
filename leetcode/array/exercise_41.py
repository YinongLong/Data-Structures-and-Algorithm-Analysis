# -*- coding: utf-8 -*-
from __future__ import print_function

class Solution(object):

    def firstMissingPositive(self, nums):
        """
        这是一个关于Array的练习，要求时间复杂度为O(n)，并且空间复杂度为常数。
        有一个方法论就是尽可能的使用题目中掌握的所有信息，这样才有更大的可能性找出
        比较满意的解决方案。在关于这个题目解决的过程中，关于Array的题目，我们很容易
        就发现有一个index的信息我们是可以利用的。
        :types nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        if len_nums == 1:
            return 1 if nums[0] != 1 else 2
        for i in range(len_nums):
            cur_idx = i
            temp_num = nums[cur_idx]
            if temp_num <= 0:
                nums[cur_idx] = -1  # 用-1代表该索引位置待填充
                continue
            elif (temp_num - 1) == cur_idx:  # 代表当前索引位与数字对齐
                continue
            else:  # 代表当前索引位置的数字与索引没有对齐，则对数字代表的索引进行追踪，直到出现负数或对齐
                nums[cur_idx] = -1
                while (temp_num - 1) != cur_idx and temp_num > 0 and temp_num <= len_nums:
                    cur_idx = temp_num
                    temp_num = nums[cur_idx]
                    # 因为是通过索引找过来的，所以该位置应该对齐
                    nums[cur_idx] = cur_idx + 1

        for i in range(1, len_nums):
            if (nums[i] - 1) != i:
                return i + 1
        return len_nums + 1

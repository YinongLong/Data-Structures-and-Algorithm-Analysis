# -*- coding: utf-8 -*-
from __future__ import print_function

class Solution(object):

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 也就是说交换数字序列中的数字，使得数字序列成为紧接着下一个大于当前数字序列的序列
        len_nums = len(nums)
        if len_nums > 1:
            index = -1
            while index > (len_nums * -1):
                if nums[index] > nums[index-1]:
                    flag_index = index - 1
                    max_index = index
                    start_index = len_nums + index
                    for i in range(start_index, len_nums):
                        if nums[i] < nums[max_index] and nums[i] > nums[flag_index]:
                            max_index = i
                    nums[flag_index], nums[max_index] = nums[max_index], nums[flag_index]
                    # 对后面剩余的数字序列进行排序
                    self.sort_array(nums, start_index, len_nums)
                    break
                index -= 1
            else:
                for i in range(len_nums/2):
                    nums[i], nums[len_nums-1-i] = nums[len_nums-1-i], nums[i]

    def sort_array(self, array, start_index, length):
        """
        :type array: List[int]
        :type start_index: int
        :type length: int
        :rtype: void
        """
        for i in range(start_index+1, length):
            temp_num = array[i]
            for j in range(i-1, start_index-1, -1):
                if array[j] > temp_num:
                    array[j+1] = array[j]
                else:
                    array[j+1] = temp_num
                    break
            else:
                array[j] = temp_num

test_cases = [[1, 2, 3], [3, 2, 1], [1, 1, 5], [1, 3, 2], [1], [4, 2, 4, 5]]
s = Solution()
for item in test_cases:
    s.nextPermutation(item)
    print(item)

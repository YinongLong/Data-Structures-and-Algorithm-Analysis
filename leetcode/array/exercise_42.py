# -*- coding: utf-8 -*-
from __future__ import print_function


class Solution(object):

    def trap_two_pointers(self, height):
        if not height:
            return 0

        # delete zero elements from head and tail to center
        left_pointer = 0
        right_pointer = len(height) - 1
        while left_pointer < len(height) and height[left_pointer] == 0:
            left_pointer += 1
        while right_pointer >= 0 and height[right_pointer] == 0:
            right_pointer -= 1

        trapping_water = 0

        if left_pointer < len(height) and right_pointer >= 0:
            left_max_elevation = height[left_pointer]
            right_max_elevation = height[right_pointer]
        left_container = []
        right_container = []
        while left_pointer < right_pointer:
            # firstly, move the left pointer
            left_pointer += 1
            if left_pointer == right_pointer:
                left_sum = sum(left_container)
                right_sum = sum(right_container)
                max_diff = left_max_elevation - right_max_elevation
                if max_diff > 0:
                    left_sum -= max_diff * len(left_container)
                    left_sum = 0 if left_sum < 0 else left_sum
                if max_diff < 0:
                    right_sum += max_diff * len(right_container)
                    right_sum = 0 if right_sum < 0 else right_sum

                trapping_water += left_sum + right_sum
                break

            if height[left_pointer] >= left_max_elevation:
                trapping_water += sum(left_container)
                left_container = []
                left_max_elevation = height[left_pointer]
            else:
                left_container.append(left_max_elevation - height[left_pointer])

            # secondly, move the right pointer
            right_pointer -= 1
            if right_pointer == left_pointer:
                left_sum = sum(left_container)
                right_sum = sum(right_container)
                max_diff = left_max_elevation - right_max_elevation
                if max_diff > 0:
                    left_sum -= max_diff * len(left_container)
                    left_sum = 0 if left_sum < 0 else left_sum
                if max_diff < 0:
                    right_sum += max_diff * len(right_container)
                    right_sum = 0 if right_sum < 0 else right_sum

                trapping_water += left_sum + right_sum
                break
            if height[right_pointer] >= right_max_elevation:
                trapping_water += sum(right_container)
                right_container = []
                right_max_elevation = height[right_pointer]
            else:
                right_container.append(right_max_elevation - height[right_pointer])
        return trapping_water

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        # find the elevation, which is greater than 0
        start_idx = 0
        start_elevation = height[start_idx]
        while start_elevation == 0 and start_idx < length:
            start_idx += 1
            start_elevation = height[start_idx]

        trapping_water = 0
        if start_idx < length - 2:  # we can trap rain water at least three bar
            container = []
            for i in range(start_idx + 1, length):
                temp_elevation = height[i]
                if temp_elevation < start_elevation:
                    container.append(start_elevation - temp_elevation)
                else:
                    print(container)
                    trapping_water += sum(container)
                    start_elevation = temp_elevation
                    container = []
            if len(container) > 1:
                end_elevation = container.pop()
                while len(container) > 0:
                    temp_elevation = container.pop()
                    residual = temp_elevation - end_elevation
                    if residual > 0:
                        trapping_water += residual
        return trapping_water


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
s = Solution()
print(s.trap_two_pointers([5, 4, 1, 2]))

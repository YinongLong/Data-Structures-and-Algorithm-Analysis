# -*- coding: utf-8 -*-
from __future__ import print_function


class Solution(object):

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
print(s.trap(height))

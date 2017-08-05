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
        if start_idx < length - 2:  # we can trap rain water at least three bar
            
            for i in range(start_idx + 1, length):
                temp_elevation = height[i]

                pass
            pass
        else:
            return 0

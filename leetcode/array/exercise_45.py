# -*- coding: utf-8 -*-
from __future__ import print_function


class Node(object):

    def __init__(self, idx, level, stride):
        self.idx = idx
        self.level = level
        self.stride = stride


class Solution(object):

    def jump_matrix(self, nums):
        len_array = len(nums)
        state_mat = [[0] * len_array for i in range(len_array)]
        for i in range(len_array):
            for j in range(nums[i]+1):
                position = i + j if (i + j) < len_array else (len_array - 1)
                state_mat[i][position] = 1

        count = 0
        j = -1
        i = 0
        while j != (-len_array):
            pass
        for j in range(-1, -len_array-1, -1):
            for i in range(len_array):
                if state_mat[i][j] == 1:
                    count += 1

                else:
                    pass
                pass
            pass
        print(state_mat)

    def jump_bfs(self, nums):
        """
        using the BFS(Breadth First Search) method
        """
        len_nums = len(nums)
        access_state = [False] * len_nums
        import collections
        candidates = collections.deque()
        candidates.append(Node(0, 0, nums[0]))
        access_state[0] = True
        while len(candidates) > 0:
            temp_node = candidates.popleft()

            for i in range(temp_node.stride, 0, -1):
                next_idx = temp_node.idx + i
                next_level = temp_node.level + 1
                if next_idx == (len_nums - 1):
                    return next_level
                if (next_idx < len_nums) and (not access_state[next_idx]):
                    candidates.append(Node(next_idx, temp_node.level+1, nums[next_idx]))
                    access_state[next_idx] = True
        return 0


    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        state = [None] * len_nums
        min_steps = [None] * len_nums
        state[-1] = 0
        for i in range(-2, -len_nums-1, -1):
            if (nums[i] + i) >= -1:
                state[i] = 1
            else:
                min_step = len_nums - 1
                for j in range(i + nums[i], i, -1):
                    if state[j] < min_step:
                        min_step = state[j]
                state[i] = min_step + 1
        return state[0]


nums = [4]
s = Solution()
print(s.jump_bfs(nums))

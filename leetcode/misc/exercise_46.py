# -*- coding: utf-8 -*-
from __future__ import print_function


class Solution(object):

    def permute_backtracking(self, nums):
        """
        根据题目的提示，可以使用回溯法来生成所有的可能的结果。
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        root = {'parent': None,  # 标记该节点的父节点
                'state': list(),  # 到该节点为止的状态序列
                'positives': nums,  # 可用于生成下一个状态序列的候选集
                'negatives': list()  # 已经用于生成下一个状态序列的候选集
                }
        temp_node = root
        while temp_node is not None:
            if temp_node['positives']:
                item = temp_node['positives'].pop()
                next_node = {'parent': temp_node,
                            'state': temp_node['state'] + [item],
                            'positives': temp_node['positives'] + temp_node['negatives'],
                            'negatives': list()
                            }
                temp_node['negatives'].append(item)
                temp_node = next_node
            else:  # 如果当前节点是叶子节点，即为一种permutation的可能，则添加进结果
                if not temp_node['negatives']:
                    result.append(temp_node['state'])
                temp_node = temp_node['parent']
        return result


    def permute(self, nums):
        """
        从我们的第一直觉上来说，permutations很简单，只不过是所有数字的排列而已，
        因此总共有len(nums)!种结果。现在的问题是怎么将这么多种结果生成出来。
        在这里借用beam search的方法，按照序列的长度依次生成，并且记录中间过程可用的
        剩余元素。
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        import copy
        len_nums = len(nums)
        state = [([], copy.copy(nums))]
        for i in range(1, len_nums+1):
            temp_state = []
            for temp_nums, candidates in state:
                for item in candidates:
                    temp_state.append((temp_nums + [item]))

nums = [1, 2, 3, 4, 5, 10, 11, 12, 13]
s = Solution()
result = s.permute_backtracking(nums)
print(result)
print(len(result))

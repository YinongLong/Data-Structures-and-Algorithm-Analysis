# -*- coding: utf-8 -*-
from __future__ import print_function


class Solution(object):

    def permuteUnique(self, nums):
        """
        这个问题相比于前面permutation问题来说多了个nums中可能存在重复数字的情况，
        但是考虑之前的解法，可以在'positives'和'negatives'这里做一点修改，来保
        证避免出现重复的问题，也就是在每一个节点生成自己的孩子节点的时候，不能使用
        相同的候选项。
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        root = {'parent': None,
                'state': [],
                'positives': nums,
                'negatives': [],
                'negatives_set': set()  # 这里使用set来记录已经生成孩子节点的候选项，加速查找
                }
        temp_node = root
        result = []
        while temp_node is not None:
            if temp_node['positives']:
                item = temp_node['positives'].pop()
                if item in temp_node['negatives_set']:
                    temp_node['negatives'].append(item)
                    continue
                next_node = {'parent': temp_node,
                            'state': temp_node['state'] + [item],
                            'positives': temp_node['positives'] + temp_node['negatives'],
                            'negatives': [],
                            'negatives_set': set()}
                temp_node['negatives'].append(item)
                temp_node['negatives_set'].add(item)
                temp_node = next_node
            else:
                if not temp_node['negatives']:
                    result.append(temp_node['state'])
                temp_node = temp_node['parent']
        return result

nums = [1, 1, 2]
s = Solution()
result = s.permuteUnique(nums)
print(result)
print(len(result))

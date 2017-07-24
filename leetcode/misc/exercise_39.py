# -*- coding: utf-8 -*-
from __future__ import print_function

import copy

class Node(object):

    def __init__(self, num, result_list, residual, parent):
        """
        初始化一个搜索树的节点
        :param num: int
            表示生成该节点的数字
        :param result_list: List[int]
            表示到达该节点路径上的数字序列
        :param residual: int
            表示生成该节点后，还剩余的数字大小
        :param parent: Node
            表示生成该节点的父节点引用
        """
        self.num = num
        self.result_list = result_list
        self.residual = residual
        self.parent = parent
        self.children = []

    def generate_children(self, nums):
        """
        生成该节点的所有的合法（剩余值大于等于0）该子节点
        :param nums: List[int]
        """
        for item in nums:
            temp_residual = self.residual - item
            if temp_residual < 0:
                continue
            temp_list = copy.copy(self.result_list)
            temp_list.append(item)
            self.children.append(Node(item, temp_list, temp_residual, self))


class Solution(object):

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        root = Node(None, [], target, None)
        root.generate_children(candidates)
        temp_node = root
        temp_result = []
        while temp_node is not None:
            if len(temp_node.children) > 0:
                # 首先进行一次检查，将所有的子节点剩余值为0的结果找到，即为一个合法值
                finished = []
                for idx, child in enumerate(temp_node.children):
                    if child.residual == 0:
                        temp_result.append(child.result_list)
                        finished.append(idx)
                temp_node.children = [temp_node.children[idx] for idx in range(len(temp_node.children)) if idx not in finished]
                if len(temp_node.children) == 0:
                    temp_node = temp_node.parent
                else:  # 说明还有节点的值剩余，因此继续将搜索树进行扩展
                    temp_node = temp_node.children.pop()
                    temp_node.generate_children(candidates)
            else:  # 说明该节点没有一个合法的子节点，需要向上回溯
                temp_node = temp_node.parent
        result = set()
        for item in temp_result:
            item.sort()
            result.add(tuple(item))
        return [list(item) for item in result]


candidates = [92,71,89,74,102,91,70,119,86,116,114,106,80,81,115,99,117,93,76,77,111,110,75,104,95,112,94,73]
target = 310
s = Solution()
print(s.combinationSum(candidates, target))

# -*- coding: utf-8 -*-
from __future__ import print_function

import copy

class Node(object):

    def __init__(self, result_list, candidates, residual, parent, depth):
        """
        初始化一个搜索树的节点
        :param result_list: List[int]
            表示到达该节点路径上的数字序列
        :param candidates: List[int]
            表示可以成为候选分支节点的数字序列
        :param residual: int
            表示生成该节点后，还剩余的数字大小
        :param parent: Node
            表示生成该节点的父节点引用
        """
        self.depth = depth
        self.result_list = result_list
        self.candidates = candidates
        self.residual = residual
        self.parent = parent
        self.children = []

    def generate_children(self):
        """
        生成该节点的所有的合法（剩余值大于等于0）该子节点
        :param nums: List[int]
        """
        temp_candidates = copy.copy(self.candidates)
        for item in self.candidates:
            temp_residual = self.residual - item
            if temp_residual >= 0:
                temp_list = copy.copy(self.result_list)
                temp_list.append(item)
                self.children.append(Node(temp_list, copy.copy(temp_candidates), temp_residual, self, self.depth+1))
            temp_candidates.remove(item)


class Solution(object):

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        root = Node([], candidates, target, None, 0)
        root.generate_children()
        temp_node = root
        temp_result = []
        while temp_node is not None:
            if len(temp_node.children) > 0:
                # 首先进行一次检查，将所有的子节点剩余值为0的结果找到，即为一个合法值
                unfinished = []
                for child in temp_node.children:
                    if child.residual == 0:  # 在这里需要清楚，只要出现一个0，就代表分支已经结束
                        temp_result.append(child.result_list)
                    else:
                        unfinished.append(child)

                temp_node.children = unfinished
                if len(unfinished) > 0:  # 说明全部都不为0，因此继续向下搜索
                    temp_node = temp_node.children.pop()
                    temp_node.generate_children()
            else:  # 说明该节点没有一个合法的子节点，需要向上回溯
                temp_node = temp_node.parent

        result = set()
        for item in temp_result:
            item.sort()
            result.add(tuple(item))
        return [list(item) for item in result]


candidates = [92,71,89,74,102,91,70,119,86,116,114,106,80,81,115,99,117,93,76,77,111,110,75,104,95,112,94,73]
target = 310
# candidates = [2, 3, 6, 7]
# target = 7
s = Solution()
print('result', s.combinationSum(candidates, target))

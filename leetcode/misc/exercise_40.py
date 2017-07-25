# -*- coding: utf-8 -*-
from __future__ import print_function

import copy

class Node(object):

    def __init__(self, result_list, residual, candidates, parent):
        self.result_list = result_list
        self.residual = residual
        self.candidates = candidates
        self.parent = parent
        self.children = []

    def generate_children(self):
        temp_candidates = copy.copy(self.candidates)
        for item in self.candidates:
            temp_candidates.remove(item)
            temp_residual = self.residual - item
            if temp_residual >= 0:
                temp_result_list = copy.copy(self.result_list)
                temp_result_list.append(item)
                self.children.append(Node(temp_result_list, temp_residual, copy.copy(temp_candidates), self))


class Solution(object):

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        root = Node([], target, candidates, None)
        root.generate_children()
        temp_node = root
        result_list = []
        while temp_node is not None:
            if len(temp_node.children) > 0:
                unfinished = []
                for child in temp_node.children:
                    if child.residual == 0:
                        child.result_list.sort()
                        result_list.append(tuple(child.result_list))
                    else:
                        unfinished.append(child)
                temp_node.children = unfinished
                if len(unfinished) > 0:
                    temp_node = temp_node.children.pop()
                    temp_node.generate_children()
            else:
                temp_node = temp_node.parent
        result = set(result_list)
        return [list(item) for item in result]


candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
s = Solution()
print(s.combinationSum2(candidates, target))

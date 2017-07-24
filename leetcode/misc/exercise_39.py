# -*- coding: utf-8 -*-
from __future__ import print_function

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
        self.children = None

    def generate_children(self, nums_node):
        """
        生成该节点的所有该子节点
        :param nums_node: List[Node]
        """
        self.children = nums


class Solution(object):

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        root = Node(None, [], target, None)

        temp_node = root
        while temp_node is not None:

            pass
    pass

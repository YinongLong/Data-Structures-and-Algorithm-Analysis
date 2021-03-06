# -*- coding: utf-8 -*-
from __future__ import print_function

from collections import defaultdict


class Node(object):

    def __init__(self, p_i=None, p_j=None, p_item=None, p=None):
        self.p_i = p_i
        self.p_j = p_j
        self.p_item = p_item
        self.p = p
        self.candidates = []

    def generate_children(self, i, j, state):
        r_info, c_info, b_info = get_location_info(i, j)
        for item in map(str, range(1, 10)):
            if not relationship(state[item], r_info, c_info, b_info):
                self.candidates.append(Node(i, j, item, self))


def get_location_info(i, j):
    return ('r%d' % i, 'c%d' % j, 'b%d%d' % (i/3, j/3))


def relationship(state_set, r_info, c_info, b_info):
    if (r_info in state_set) or (c_info in state_set) or (b_info in state_set):
        return True
    else:
        return False


class Solution(object):

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        size = len(board)

        # 首先统计整个数独board的信息
        state = defaultdict(set)
        locations = []
        for i in range(size):
            row = board[i]
            for j in range(size):
                item = row[j]
                if item == '.':
                    locations.append((i, j))
                for info in get_location_info(i, j):
                    state[item].add(info)

        root = Node()
        temp_node = root
        index = 0
        generate = True
        while index < len(locations):
            if generate:
                loc_i, loc_j = locations[index]
                temp_node.generate_children(loc_i, loc_j, state)
            if len(temp_node.candidates) > 0:
                child = temp_node.candidates.pop()
                # 对于挑选出的子节点，需要更新状态信息，并且在后面回撤的过程中需要删除信息
                for info in get_location_info(child.p_i, child.p_j):
                    state[child.p_item].add(info)
                temp_node = child
                index += 1
                generate = True
            else:
                generate = False
                index -= 1
                # 将整个状态返回至生成该节点之前的状态
                for info in get_location_info(temp_node.p_i, temp_node.p_j):
                    state[temp_node.p_item].remove(info)
                temp_node = temp_node.p
        # 说明答案已经找到，现在只需要按照树的路径回溯回去即可
        while temp_node.p is not None:
            board[temp_node.p_i][temp_node.p_j] = temp_node.p_item
            temp_node = temp_node.p

# -*- coding: utf-8 -*-
from __future__ import print_function


class Solution(object):

    def __init__(self):
        self.stack = []
        self.heap = []

    def _maintain_heap(self):
        len_heap = len(self.heap)
        for i in range((len_heap - 1)/2, -1, -1):
            self._update_heap(i, len_heap)

    def _update_heap(self, index, length):
        left_child = index * 2 + 1
        if left_child < length:
            temp = self.heap[index]
            if (left_child + 1) < length and (self.heap[left_child][0] > self.heap[left_child + 1][0]):
                left_child += 1
            if self.heap[left_child][0] < temp[0]:
                self.heap[index] = self.heap[left_child]
                self.heap[left_child] = temp
                self._update_heap(left_child, length)

    def push(self, node):
        item = [node, 1]
        self.stack.append(item)
        self.heap.insert(0, item)
        self._update_heap(0, len(self.heap))

    def pop(self):
        item = self.stack.pop()
        item[1] = 0
        return item[0]

    def top(self):
        return self.stack[-1][0]

    def min(self):
        while self.heap[0][1] == 0:
            self.heap = self.heap[1:]
            self._maintain_heap()
        return self.heap[0][0]


s = Solution()
s.push(3)
s.push(2)
s.push(4)
s.push(10)
s.push(1)
print('top', s.top())
print('min', s.min())
print('pop', s.pop())
print('pop', s.pop())
print('min', s.min())

# -*- coding: utf-8 -*-
from __future__ import print_function

class Solution(object):

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def push(self, node):
        self.stack_1.append(node)

    def pop(self):
        if self.stack_2:
            return self.stack_2.pop()
        else:
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())
            return self.stack_2.pop()


s = Solution()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)

print(s.pop())
print(s.pop())
print(s.pop())
s.push(6)
print(s.pop())
print(s.pop())
print(s.pop())

# -*- coding: utf-8 -*-
from __future__ import print_function


class Solution(object):

    def __init__(self):
        self.max_num = None
        self.records = dict()

    def generate_next(self, prev_str):
        count = 0
        prev = None
        result = []
        for item in prev_str:
            if prev is None:
                prev = item
                count += 1
            elif item == prev:
                count += 1
            else:
                result.append(str(count))
                result.append(prev)
                prev = item
                count = 1
        if count > 0:
            result.append(str(count))
            result.append(prev)
        return ''.join(result)

    def countAndSay(self, n):
        if self.max_num is None:
            self.max_num = n
            prev_str = None
            for i in range(n):
                if prev_str is None:
                    prev_str = '1'
                else:
                    prev_str = self.generate_next(prev_str)
                self.records[i+1] = prev_str
        elif n > self.max_num:
            prev_str = self.records[self.max_num]
            for i in range(self.max_num + 1, n + 1):
                prev_str = self.generate_next(prev_str)
                self.records[i] = prev_str
        return self.records[n]



s = Solution()
print(s.countAndSay(100000))

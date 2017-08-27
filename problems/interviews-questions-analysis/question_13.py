# -*- coding: utf-8 -*-
from __future__ import print_function

class Solution(object):

    def Fibonacci(self, n):
        """
        这道题目需要输出斐波那契数列的第n项，这是一道常规题目，只需要避免使用
        递归的坑就成功了大半。因为Fibonacci数是前两项数字的和，因此，只需要记录
        前两个数字，直接循环解决就可以，如果考虑到程序测试的多次调用，还可以在对象
        内部保存已经计算到的相关结果，以方便下一次计算。
        """
        last_but_one = 0
        last_one = 1
        if n == 0:
            return last_but_one
        elif n == 1:
            return last_one
        else:
            idx = 2
            while idx <= n:
                next_val = last_but_one + last_one
                last_but_one = last_one
                last_one = next_val
                idx += 1
            return next_val


s = Solution()
print(s.Fibonacci(0))

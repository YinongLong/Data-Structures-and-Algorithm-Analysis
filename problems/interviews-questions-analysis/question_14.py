# -*- coding: utf-8 -*-
from __future__ import print_function

class Solution(object):

    def jumpFloor(self, number):
        """
        这道题目是有一个共有number级的台阶，一个青蛙一次可以跳上1级台阶或2级台阶，问青蛙共有多少种跳法。
        对于这个问题，我们立马就会想到一个递归的解法，假如函数f会返回青蛙跳n级台阶共有多少种跳法的结果，
        那么我们有如下的递推公式
        f(number) = f(number-1) + f(number-2)
        但是从这个递推公式中我们会发现里面存在类似Fibonacci数列的递归解的问题，就是将一个同样的计算多次的
        进行递归解决，这会存在指数级别的计算量增长。因此，类似于Fibonacci的解法，我们可以利用一个简单的动态
        规划的方法来做。因为我们知道当f(0)=1（代表站在原地就好）, f(1)=1, f(2)=f(1)+f(0)=2, f(3)=f(2)+f(1)=3
        依次类推就可以计算出f(number)
        """
        state = [1, 1]
        for i in range(number+1):
            if i < 2:
                continue
            else:
                state.append(state[i-1] + state[i-2])
        return state[number]

# -*- coding: utf-8 -*-
from __future__ import print_function


class Solution(object):

    def _verify(self, sequence):
        if sequence:
            temp = sequence.pop()
            flag_idx = -1
            for idx, item in enumerate(sequence):
                if item > temp:
                    flag_idx = idx
                if flag_idx != -1 and item < temp:
                    return False
            if flag_idx == -1:
                return self._verify(sequence)
            left_re = self._verify(sequence[0:flag_idx])
            right_re = self._verify(sequence[flag_idx:])
            return left_re and right_re
        return True

    def VerifySquenceOfBST(self, sequence):
        if sequence:
            return self._verify(sequence)
        else:
            return False



s = Solution()
print(s.VerifySquenceOfBST([1, 5, 4, 7, 10, 6]))
print(s.VerifySquenceOfBST([1, 2, 3, 4, 5]))
print(s.VerifySquenceOfBST([5, 4, 3, 2, 1]))
print(s.VerifySquenceOfBST([7, 4, 6, 5]))

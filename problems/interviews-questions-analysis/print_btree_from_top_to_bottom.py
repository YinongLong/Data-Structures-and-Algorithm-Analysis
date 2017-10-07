# -*- coding: utf-8 -*-
from __future__ import print_function


class Solution(object):

    def PrintFromTopToBottom(self, root):
        candidates = []
        result = []
        if root:
            candidates.append(root)
            while candidates:
                temp = candidates.pop(0)
                result.append(temp.val)
                if temp.left:
                    candidates.append(temp.left)
                if temp.right:
                    candidates.append(temp.right)

        return result

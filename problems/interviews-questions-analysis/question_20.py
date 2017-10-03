# -*- coding: utf-8 -*-
from __future__ import print_function

from utils import ListNode

class Solution(object):

    def FindKthToTail(self, head, k):
        temp_stack = []
        while head:
            temp_stack.append(head)
            head = head.next

        if k > len(temp_stack) or k == 0:
            return None

        for i in range(k - 1):
            temp_stack.pop()

        return temp_stack.pop()

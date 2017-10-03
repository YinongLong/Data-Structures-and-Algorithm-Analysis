# -*- coding: utf-8 -*-
from __future__ import print_function

class Solution(object):

    def ReverseList(self, pHead):

        prev = None
        while pHead:
            temp_next = pHead.next
            pHead.next = prev
            prev = pHead
            pHead = temp_next

        return prev

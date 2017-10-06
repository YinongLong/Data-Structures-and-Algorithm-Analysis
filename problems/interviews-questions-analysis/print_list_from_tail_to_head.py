# -*- coding: utf-8 -*-
from __future__ import print_function

class Solution(object):

    def printListFromTailToHead(self, listNode):
        temp_list = []
        head = listNode
        while head:
            temp_list.append(head.val)
            head = head.next
        result = []
        while temp_list:
            result.append(temp_list.pop())
        return result

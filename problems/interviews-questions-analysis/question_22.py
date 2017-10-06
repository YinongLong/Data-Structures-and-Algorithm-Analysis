# -*- coding: utf-8 -*-
from __future__ import print_function

from utils import ListNode

class Solution(object):

    def Merge(self, pHead1, pHead2):

        prev_head1 = ListNode(None)
        prev_head1.next = pHead1

        curr_head1 = pHead1
        curr_head2 = pHead2

        pHead1 = prev_head1
        while curr_head1 and curr_head2:
            if curr_head1.val >= curr_head2.val:
                prev_head1.next = curr_head2
                curr_head2 = curr_head2.next
                prev_head1.next.next = curr_head1
                prev_head1 = prev_head1.next
            else:
                curr_head1 = curr_head1.next
                prev_head1 = prev_head1.next

        if curr_head1 is None:
            prev_head1.next = curr_head2
        return pHead1.next

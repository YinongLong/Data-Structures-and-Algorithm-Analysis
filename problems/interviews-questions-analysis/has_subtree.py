# -*- coding: utf-8 -*-
from __future__ import print_function

from utils import TreeNode

class Solution(object):

    def _pre_order_traversal(self, root, substring):
        if root:
            substring += str(root.val)
            substring = self._pre_order_traversal(root.left, substring)
            substring = self._pre_order_traversal(root.right, substring)
        return substring

    def _in_order_traversal(self, root, substring):
        if root:
            substring = self._in_order_traversal(root.left, substring)
            substring += str(root.val)
            substring = self._in_order_traversal(root.right, substring)
        return substring

    def HasSubtree(self, pRoot1, pRoot2):
        pRoot1_str = self._pre_order_traversal(pRoot1, '')
        pRoot2_str = self._pre_order_traversal(pRoot2, '')
        if pRoot2_str == '':
            return False

        if pRoot1_str.find(pRoot2_str) == -1:
            return False
        return True

    def HasSubtree_v2(self, pRoot1, pRoot2):
        pass


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
n8 = TreeNode(8)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n5.left = n7
n5.right = n8
n3.right = n6

s = Solution()
print(s._in_order_traversal(n1, ''))

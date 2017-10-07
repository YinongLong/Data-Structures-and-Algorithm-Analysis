# -*- coding: utf-8 -*-
from __future__ import print_function

from utils import TreeNode

class Solution(object):

    def FindPath(self, root, expectNumber):
        result = []
        def pre_order_traversal(node, path, residual):
            residual -= node.val
            if residual >= 0:
                if (node.left == node.right == None) and (residual == 0):  # leaf node
                    result.append(path + [node.val])
                if node.left and residual > 0:
                    pre_order_traversal(node.left, path + [node.val], residual)
                if node.right and residual > 0:
                    pre_order_traversal(node.right, path + [node.val], residual)

        if root is None:
            return []
        pre_order_traversal(root, [], expectNumber)
        return result

n1 = TreeNode(10)
n2 = TreeNode(5)
n3 = TreeNode(12)
n4 = TreeNode(4)
n5 = TreeNode(7)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
s = Solution()
print(s.FindPath(n1, 22))

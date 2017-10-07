# -*- coding: utf-8 -*-
from __future__ import print_function

class Solution(object):

    def _exchange_children(self, root):
        if root:
            root.left, root.right = root.right, root.left
            self._exchange_children(root.left)
            self._exchange_children(root.right)

    def Mirror(self, root):
        """
        这里的镜像二叉树经过分析，其实就是递归式的将每一个根结点的左右孩子相互之间
        进行交换而已。
        """
        self._exchange_children(root)
        return root

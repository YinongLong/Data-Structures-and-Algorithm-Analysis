# -*- coding: utf-8 -*-
from __future__ import print_function


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def reConstructBinaryTree(self, pre, tin):
        """
        根据二叉树的中序遍历和先序遍历来构建整个二叉树
        开始思考的时候是直接模拟手动解决时候的做法，从先序找划分节点，然后对中序遍历的结果
        进行划分生成子树。但是突然意识到，这完全就是一个递归的问题呀。

        Parameters
        ----------
        pre: List[int]
            先序遍历的数字列表

        tin: List[int]
            中序遍历的数字列表

        Returns
        -------
        TreeNode
        """
        root_val = pre.pop(0)
        left_children = []
        right_children = None
        for idx, val in enumerate(tin):
            if val == root_val:
                right_children = tin[(idx+1):]
                break
            left_children.append(val)
        root = TreeNode(root_val)
        if left_children:
            root.left = self.reConstructBinaryTree(pre, left_children)
        if right_children:
            root.right = self.reConstructBinaryTree(pre, right_children)
        return root

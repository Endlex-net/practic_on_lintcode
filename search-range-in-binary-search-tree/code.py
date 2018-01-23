#-*-coding: utf-8 -*-
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: param root: The root of the binary search tree
    @param: k1: An integer
    @param: k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def searchRange(self, root, k1, k2):
        # write your code here
        l = []
        quene = []
        if root:
            quene.append(root)
            while quene:
                cur_node = quene.pop(0)
                l.append(cur_node.val)
                if cur_node.right:
                    quene.append(cur_node.right)
                if cur_node.left:
                    quene.append(cur_node.left)
        l = filter(lambda x: x>=k1 and x <=k2, l)
        l.sort()
        return l
#-*- coding:utf-8 -*-
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        # write your code here
        l = []
        quene = [root]
        while quene:
            cur_root = quene.pop(0)
            if cur_root:
                l.append(cur_root.val)
                quene.append(cur_root.left)
                quene.append(cur_root.right)
            else:
                l.append('')
        st = ','.join([str(i) for i in l])
        return st
        

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """
    def deserialize(self, data):
        # write your code here
        l = data.split(',')
        val = l.pop(0)
        if val == "":
            return None
        quene = []
        root = TreeNode(val)
        quene.append(root)
        while quene:
            cur_root = quene.pop(0)
            left = l.pop(0)
            right = l.pop(0)
            cur_root.left = TreeNode(left) if left else None
            if left:
                quene.append(cur_root.left)
            
            cur_root.right = TreeNode(right) if right else None
            if right:
                quene.append(cur_root.right)
        return root
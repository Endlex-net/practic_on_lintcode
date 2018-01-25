#-*-coding: utf-8 -*- 
"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the reversed linked list. 
                  Reverse it in-place.
    """
    def reverse(self, head):
        # write your code here
        now = head
        temp = None
        while now:
            next = now.next
            now.next = temp
            temp = now
            now = next
        return temp
#-*-coding:utf-8 -*-
class Solution:
    """
    @param: str: An array of char
    @param: offset: An integer
    @return: nothing
    """
    def rotateString(self, str, offset):
        # write your code here
        if not str:
            return
        for i in xrange(offset%len(str)):
            str.insert(0, str.pop(-1))
#-*-coding: utf-8 -*-
class Solution:
    def strStr(self, source, target):
        if source == None or target == None:
            return -1
        return source.find(target)

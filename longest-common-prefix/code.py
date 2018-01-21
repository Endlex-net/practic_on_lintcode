#-*- coding: utf-8 -*-
class Solution:
    # @param strs: A list of strings
    # @return: The longest common prefix
    def longestCommonPrefix(self, strs):
        # write your code here
        if not strs:
            return ""
        min_len = min(map(lambda l: len(l), strs))
        i = 0
        while i < min_len:
            if not reduce((lambda x, y: x and y), map((lambda x: x[:i+1] == strs[0][:i+1]), strs)):
                break
            i += 1
        return strs[0][:i]
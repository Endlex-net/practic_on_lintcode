# -*-coding: utf-8 -*-
class Solution:
    # @param strs: A list of strings
    # @return: A list of strings
    def anagrams(self, strs):
        sl2count = {}
        sl2lists = {}
        l = []
        for s in strs:
            sl = list(s)
            sl.sort()
            sl = str(sl)
            sl2count[sl] = sl2count.get(sl,0) + 1
            sl2lists.setdefault(sl, []).append(s)
        for k in sl2count:
            if sl2count[k] > 1:
                l += sl2lists[k]
        return l
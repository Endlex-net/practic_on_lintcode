# -*-coding: utf-8 -*-
class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """
    def anagram(self, s, t):
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        return s == t
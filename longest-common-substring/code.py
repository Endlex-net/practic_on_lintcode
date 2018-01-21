#-*- coding: utf-8 -*-
class Solution:
    """
    @param: A: A string
    @param: B: A string
    @return: the length of the longest common substring.
    """
    def longestCommonSubstring(self, A, B):
        # write your code here
        if len(A) > len(B):
            A, B = B, A
        start = 0
        last = 1
        A_count = len(A)
        max_len = 0
        while start < A_count and last <= A_count:
            while last <= A_count:
                if A[start: last] not in B:
                    start += 1
                    last = start + max(max_len, 0) 
                    break
                max_len = last - start
                last += 1
        return max_len
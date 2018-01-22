#-*- coding: utf-8 -*-
class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        A.sort()
        return A[len(A) - k]
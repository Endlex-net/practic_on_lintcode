#-*- coding:utf-8 -*-
class Solution:
    """
    @param: A: sorted integer array A
    @param: B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        # write your code here
        C = []
        while A and B:
            if A[0] < B[0]:
                C.append(A.pop(0))
            else:
                C.append(B.pop(0))
        if A:
            C += A
        if B:
            C += B
        return C
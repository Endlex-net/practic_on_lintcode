#-*-coding: utf-8 -*-
class Solution:
    """
    @param: : An integer
    @param: : An integer
    @return: An integer denote the count of digit k in 1..n
    """

    def digitCounts(self, k, n):
        num = 0
        st = ''.join([str(i) for i in xrange(n+1)])
        for i in st:
            if i == str(k):
                num += 1
        return num 
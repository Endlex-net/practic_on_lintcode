#-*- coding:utf-8 -*-
class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """
    def trailingZeros(self, n):
        # write your code here, try to do it without arithmetic operators.
        num = 0
        temp = 5
        while temp < n:
            num += n / temp
            temp *= 5
        return num
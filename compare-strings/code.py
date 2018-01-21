# -*- coding: utf-8 -*-
class Solution:
    """
    @param A : A string includes Upper Case letters
    @param B : A string includes Upper Case letters
    @return :  if string A contains all of the characters in B return True else return False
    """
    def compareStrings(self, A, B):
        a = list(A)
        for i in B:
            if i not in a:
                return False
            a.remove(i)
        return True
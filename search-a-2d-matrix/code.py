# -*- coding:utf-8 -*-
class Solution:
    """
    @param: matrix: matrix, a list of lists of integers
    @param: target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix:
            return False
        len_y = len(matrix)
        if len_y > 1:
            if matrix[len_y/2][0] <= target:
                return self.searchMatrix(matrix[len_y/2:], target)
            else:
                return self.searchMatrix(matrix[:len_y/2], target)
        return target in matrix[0]
                    
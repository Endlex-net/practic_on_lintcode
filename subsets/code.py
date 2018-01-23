#-*-coding: utf-8 -*-
class Solution:
    
    """
    @param: nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        if nums:
            last_subsets = self.subsets(nums[1:])
            def fun(x, y):
                l = x + y
                l.sort()
                return l
            return last_subsets + map(lambda x: fun([nums[0]],x), last_subsets)
        return [[]]
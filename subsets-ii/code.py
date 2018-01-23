#-*- coding: utf-8 -*-
class Solution:
    """
    @param: nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        # write your code here
        if nums:
            last_subsets = self.subsetsWithDup(nums[1:])
            l = last_subsets[:]
            for i in last_subsets:
                temp = i + [nums[0]]
                temp.sort()
                if temp not in l:
                    l.append(temp)
            return l
        return [[]]
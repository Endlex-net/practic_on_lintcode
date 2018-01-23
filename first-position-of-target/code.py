#-*-coding: utf-8 -*-
class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0 
    def binarySearch(self, nums, target):
        # write your code here
        s = 0
        e = len(nums)
        while e - s > 1:
            i = (s + e) / 2
            if nums[i] > target:
                e = i
            elif nums[i] < target:
                s = i
            else:
                while nums[i-1] == target:
                    i -= 1
                return i

        if nums[s] == target:
            return s
        return -1
#-*- coding:utf-8 -*-
class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        # write your code here
        def insert_num_in_nums(nums, num):
            new_nums = []
            for i in xrange(len(nums)+1):
                temp = nums[:]
                temp.insert(i, num)
                new_nums.append(temp)
            return new_nums
        l = []
        if len(nums) > 1:
            temp = reduce(lambda x, y: x + y ,map(lambda x: insert_num_in_nums(x,nums[0]), self.permuteUnique(nums[1:])))
            for i in temp:
                if i not in l:
                    l.append(i)
            return l
        l.append(nums)
        return l
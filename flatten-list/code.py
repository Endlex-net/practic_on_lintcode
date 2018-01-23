#-*- coding:utf-8 -*-
class Solution(object):

    # @param nestedList a list, each element in the list 
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        # Write your code here
        if isinstance(nestedList, int):
            return [nestedList]
        l = []
        while nestedList:
            i = nestedList.pop(0)
            if isinstance(i, int):
                l.append(i)
            if isinstance(i, list):
                l += self.flatten(i)
        return l
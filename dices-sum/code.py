#-*- coding utf-8 -*-
class Solution:
    # @param {int} n an integer
    # @return {tuple[]} a list of tuple(sum, probability)
    def dicesSum(self, n):
        # Write your code here
        c = 1 / 6.
        once_dices = [[x, c] for x in xrange(1,7)]
        dices2probability = {}
        if n < 1:
            [[]]
        if n == 1:
            return once_dices
        last_dices_sum = self.dicesSum(n-1)
        for i in once_dices:
            for j in last_dices_sum:
                dices2probability[i[0]+j[0]] = dices2probability.get(i[0]+j[0], 0) + i[1] * j[1]
        print(dices2probability)
        return  [[x,y] for x, y in dices2probability.items()]
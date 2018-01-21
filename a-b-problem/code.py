class Solution:
    """
    @param: a: An integer
    @param: b: An integer
    @return: The sum of a and b
    """
    def aplusb(self, a, b):
        l = [a, b]
        return sum(l)

# OR
class Solution:
    """
    @param: a: An integer
    @param: b: An integer
    @return: The sum of a and b
    """
    def aplusb(self, a, b):
        if a == 0:
            return b
        if b == 0:
            return a
        c = a ^ b
        d = (a&b) <<1
        self.aplusb(d, c)
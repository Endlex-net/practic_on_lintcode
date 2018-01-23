class MinStack:
    
    def __init__(self):
        # do intialization if necessary
        self.l = []

    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, number):
        # write your code here
        self.l.append(number)
    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        if self.l :
            return self.l.pop(-1)
    """
    @return: An integer
    """
    def min(self):
        # write your code here
        l = self.l
        if l:
            temp = l [0]
            for i in l:
                if i < temp:
                    temp =i
            return temp
        return None

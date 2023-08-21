class Solution(object):

    def reverseDigits(self, x:int) -> int:
        if (x < 0):
            return False
        digit = x
        reversed = 0
        while(digit != 0):
            number = digit % 10
            reversed = reversed * 10 + number
            digit = digit /10
        if (reversed == x):
            return True
        else:
            return False
        
         




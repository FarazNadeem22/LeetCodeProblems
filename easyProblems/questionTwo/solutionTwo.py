class Solution(object):

    def reverseDigits(self, number:int) -> int:
        numDigits = len(str(number))//2
        reversedNum = 0

        powerOfTen = 10 ** numDigits
        digit = number % powerOfTen

        # Reverse this 
        while digit != 0:
            number = digit % 10
            reversedNum = reversedNum * 10 + number
            digit = digit //10 

        return reversedNum


    def isPalindrome(self, x:int) -> bool:
        numDigits = len(str(x))//2
        numberOfDigits = len(str(x))
        # Take care of edge cases 
        if (numberOfDigits == 1):
            return True
        elif (numberOfDigits == 2):
            firstDigit = x // 10
            secondDigit = x % 10
            if firstDigit == secondDigit:
                return True
            else:
                return False
        # Lets get to the problem
        powerOfTen = 10 ** numDigits
        firstHalf = x % powerOfTen
        secondHalf = self.reverseDigits(x)

        if firstHalf == secondHalf:
            return True
        else:
            return False
        






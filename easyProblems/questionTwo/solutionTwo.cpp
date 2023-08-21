#include <string> 
#include <cmath>
#include <iostream>

class Solution {
public:
    bool isPalindrome(int x) 
    {
        int numDigits = std::to_string(x).size()/2;
        int numberOfDigitsTotal = std::to_string(x).size();
        if ( numberOfDigitsTotal < 3)
        {
            if (numberOfDigitsTotal == 1)
            {
                return true;
            }
            else if (numberOfDigitsTotal == 2)
            {
                std::cout<<"We are here.\n";
                int firstDigit = x /10;
                int secondDigit = x % 10;
                if (firstDigit == secondDigit)
                {
                    return true;
                }
                else
                {
                    return false;
                }

            }

        }   
        
        int powerOfTen = std::pow(10 , numDigits);
        int firstHalf = x % powerOfTen;
        if (firstHalf == reversedDigit(x))
        {
            return true;
        }
        else
        {
            return false;
        }
    }

    int reversedDigit(int number)
    {
        int numDigits = std::to_string(number).size()/2;
        int reversed = 0;

        int powerOfTen = std::pow(10, numDigits);
        int digit = number % powerOfTen;
        //std::cout << number << " % " << powerOfTen << " = " << digit << std::endl;

        while (digit != 0)
        {
            int number = digit % 10;
            reversed = reversed * 10 + number;
            digit = digit /10;
        }

        //std::cout<< "Reversed = " << reversed <<std::endl;
        return reversed;
    }
};

int main()
{
    Solution solution;
    std::cout<<solution.isPalindrome(10);
    return 0;
}
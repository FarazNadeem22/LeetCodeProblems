class Solution:
    def reverseWords(self, s: str) -> str:
        wordList = s.split()
        wordList.reverse()
        for words in wordList:
            wordList.append(" ")
        print(wordList)
        return ''.join(wordList)

       



# Driver code
solution = Solution()

input_str = "Hello World"
reversed_str = solution.reverseWords(input_str)

print("Original:", input_str)
print("Reversed:", reversed_str)
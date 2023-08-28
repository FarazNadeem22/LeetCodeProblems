from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        flowerbed = [0] + flowerbed + [0]

        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] == 1:
                continue
            if flowerbed[i - 1] == flowerbed[i + 1] == 0:
                n -= 1
                flowerbed[i] = 1

        return n <= 0

# Driver code
if __name__ == "__main__":
    solution = Solution()
    
    flowerbed = [1, 0, 0, 0, 1]
    n = 1
    result = solution.canPlaceFlowers(flowerbed, n)
    print(f"Can place {n} flowers? {result}")  # Output: Can place 1 flowers? True
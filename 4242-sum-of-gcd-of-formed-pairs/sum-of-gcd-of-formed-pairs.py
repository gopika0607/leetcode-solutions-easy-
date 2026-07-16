from math import gcd
from typing import List

class Solution:
    def gcdSum(self, nums: List[int]) -> int:
        prefixGcd = []
        mx = 0

        for num in nums:
            mx = max(mx, num)
            prefixGcd.append(gcd(num, mx))

        prefixGcd.sort()

        left, right = 0, len(prefixGcd) - 1
        ans = 0

        while left < right:
            ans += gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1

        return ans
        
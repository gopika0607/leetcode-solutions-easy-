from typing import List
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

    
        cnt = [0] * (mx + 1)
        for g in range(1, mx + 1):
            for multiple in range(g, mx + 1, g):
                cnt[g] += freq[multiple]


        exact = [0] * (mx + 1)
        for g in range(mx, 0, -1):
            pairs = cnt[g] * (cnt[g] - 1) // 2
            exact[g] = pairs
            for multiple in range(g * 2, mx + 1, g):
                exact[g] -= exact[multiple]

        prefix = []
        values = []
        total = 0
        for g in range(1, mx + 1):
            if exact[g]:
                total += exact[g]
                prefix.append(total)
                values.append(g)

        ans = []
        for q in queries:
            idx = bisect_right(prefix, q)
            ans.append(values[idx])

        return ans
        
class Solution:
    def minRemoval(self, nums, k):
        nums.sort()
        n = len(nums)

        l = 0
        max_len = 1

        for r in range(n):
            while nums[r] > nums[l] * k:
                l += 1
            max_len = max(max_len, r - l + 1)

        return n - max_len

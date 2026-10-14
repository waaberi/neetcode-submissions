from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        memo: list[int] = [None] * len(nums)

        def rec(idx):
            if idx >= len(nums):
                return 0
            if memo[idx] is not None:
                return memo[idx]
            
            memo[idx] = nums[idx] + max(rec(idx + 2), rec(idx + 3))

            return memo[idx]
        
        return max(rec(0), rec(1))
from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        memo: list[int] = [0] * (len(nums) + 3)

        # def rec(idx):
        #     if idx >= len(nums):
        #         return 0
        #     if memo[idx] is not None:
        #         return memo[idx]
        #     memo[idx] = nums[idx] + max(rec(idx + 2), rec(idx + 3))
        #     return memo[idx]
        # rec(0)
        # rec(1)

        for idx in range(len(nums) - 1, -1, -1):
            memo[idx] = nums[idx] + max(memo[idx + 2], memo[idx + 3])

        return max(memo[0], memo[1])
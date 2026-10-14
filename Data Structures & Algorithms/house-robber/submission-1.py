from functools import cache

def _rob(nums: list[int]) -> int:
    @cache
    def rec(idx):
        if idx >= len(nums):
            return 0
        return nums[idx] + max(rec(idx + 2), rec(idx + 3))
    
    return max(rec(0), rec(1))

class Solution:
    def rob(self, nums: List[int]) -> int:
        return _rob(nums)
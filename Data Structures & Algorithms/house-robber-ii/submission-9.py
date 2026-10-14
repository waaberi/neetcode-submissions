"""
5, 2, 12, 9, 10
"""

from functools import cache


def _rob(nums: List[int]) -> int:
    @cache
    def rec(idx, started_at_zero):
        if idx >= len(nums):
            return 0

        op1 = rec(idx + 2, started_at_zero) if not (started_at_zero and idx + 2 == len(nums) - 1) else 0
        
        op2 = rec(idx + 3, started_at_zero) if not (started_at_zero and idx + 3 == len(nums) - 1) else 0

        return nums[idx] + max(op1, op2)

    return max(rec(0, True), rec(1, False), rec(2, False))

class Solution:
    def rob(self, nums: List[int]) -> int:
        return _rob(nums)
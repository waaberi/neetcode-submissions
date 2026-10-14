"""
5, 2, 12, 9, 10
"""

from functools import cache


def _rob(nums: List[int]) -> int:
    @cache
    def rec(idx, started_at):
        if idx >= len(nums):
            return 0

        op1 = rec(idx + 2, started_at) if not (started_at == 0 and idx + 2 == len(nums) - 1) else 0
        
        op2 = rec(idx + 3, started_at) if not (started_at == 0 and idx + 3 == len(nums) - 1) else 0

        return nums[idx] + max(op1, op2)
    print(rec(0, 0), rec(1, 1))
    return max(rec(0, 0), rec(1, 1))

class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(_rob(nums), _rob(list(reversed(nums))))
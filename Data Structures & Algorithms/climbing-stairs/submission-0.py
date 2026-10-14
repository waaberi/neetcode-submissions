"""
30

1 + 2
1 + 1


2 + 1
2 + 2
"""


from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def distinct_branches(idx: int) -> int:
            if idx == n:
                return 1
            if idx > n:
                return 0

            return distinct_branches(idx + 1) + distinct_branches(idx + 2)

        return distinct_branches(0)
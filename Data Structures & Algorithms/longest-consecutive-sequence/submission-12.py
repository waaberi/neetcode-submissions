from functools import cache

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s: set[int] = set(nums)

        if len(nums) == 0:
            return 0

        m = 1

        for n in nums:
            if n - 1 in s:
                continue

            c = 1
            x = n + 1
            while x in s:
                x += 1
                c += 1

            m = max(m, c)

        return m

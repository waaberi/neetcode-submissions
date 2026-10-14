from functools import cache

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s: set[int] = set(nums)
        
        m = 0

        for n in nums:
            if n - 1 in s:
                continue

            x = n + 1
            while x in s:
                x += 1

            m = max(m, x-n)

        return m

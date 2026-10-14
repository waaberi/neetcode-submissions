class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []: return 0

        s_nums = set(nums)
        num = min(nums)

        sols=[0]

        while num <= max(nums):
            if num in s_nums:
                sols[-1] += 1
            else:
                sols.append(0)
            num += 1

        return max(sols)
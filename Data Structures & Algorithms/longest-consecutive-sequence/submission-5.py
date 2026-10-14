class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []: return 0


        minum = min(nums)
        maxum = max(nums)

        s_nums = set(nums)

        num = minum

        sols=[0]

        while num < maxum + 1:
            if num in s_nums:
                sols[-1] += 1
            else:
                sols.append(0)
            num += 1

        return max(sols)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        replacement_adjustment = 0
        for i, n in enumerate(nums):
            nums[i - replacement_adjustment] = nums[i]
            if n == val:
                replacement_adjustment += 1
        # print(nums)
        return len(nums) - replacement_adjustment
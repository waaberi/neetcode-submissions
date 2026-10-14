class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        replacement_adjustment = 0
        for i in range(len(nums)):
            nums[i - replacement_adjustment] = nums[i]
            if nums[i] == val:
                replacement_adjustment += 1
        # print(nums)
        return len(nums) - replacement_adjustment
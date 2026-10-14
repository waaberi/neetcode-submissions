class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        replacement_adjustment = 0
        adjusted_pos = 0
        for i in range(len(nums)):
            # adjusted_pos = i - replacement_adjustment
            if nums[i] != val:
                nums[adjusted_pos] = nums[i]
                adjusted_pos += 1
        return adjusted_pos
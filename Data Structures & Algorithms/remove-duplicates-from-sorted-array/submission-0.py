class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        decalage = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                decalage += 1
            nums[i-decalage] = nums[i]
        return len(nums) - decalage
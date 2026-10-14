class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        place_to_put_in = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[place_to_put_in] = nums[i]
                place_to_put_in += 1
        return place_to_put_in
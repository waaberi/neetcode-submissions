class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)

        first, second, third = nums[n - 2] == nums[n - 1], False, True

        for i in range(n - 3, -1, -1):
            has_two_eq = nums[i] == nums[i + 1]
            has_three_eq = nums[i] == nums[i + 1] == nums[i + 2]
            has_three_incr = nums[i] + 1 == nums[i + 1] == nums[i + 2] - 1
            
            new_first = (has_two_eq and second) or ((has_three_eq or has_three_incr) and third)

            first, second, third = new_first, first, second

        return first
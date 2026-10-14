class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = 1
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
            else: res *= num

        if zero_count == 0:
            return [res//num for num in nums]
        elif zero_count == 1:
            return [res if num == 0 else 0 for num in nums]
        else: return [0] * len(nums)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        left = 0
        right = n - 1

        while left < right:
            middle = (left + right) // 2
            if nums[middle] > nums[right]: # minimum is to the right
                left = middle + 1
            else: # minimum is middle or left
                right = middle

        offset = left

        left = 0
        right = n - 1

        while left <= right:
            middle = (left + right) // 2
            real_index = (middle + offset) % n
            val = nums[real_index]
            if val == target:
                return real_index
            elif val > target:
                right = middle - 1
            else: # smaller
                left = middle + 1

        return -1

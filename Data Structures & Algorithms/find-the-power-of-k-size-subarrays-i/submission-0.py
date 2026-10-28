class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        consecutive_streak = 1
        output = []

        for i in range(1, len(nums)):
            if nums[i] - 1 == nums[i - 1]:
                consecutive_streak += 1
            else:
                consecutive_streak = 1
            if i >= k - 1:
                output.append(nums[i] if consecutive_streak >= k else -1)

        return output

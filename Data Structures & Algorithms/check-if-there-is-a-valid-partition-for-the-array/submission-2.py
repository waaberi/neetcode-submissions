class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)

        dp: list[bool] = [False for _ in range(n + 2)]
        dp[n] = True
        dp[n - 2] = nums[n - 2] == nums[n - 1]

        for i in range(n - 3, -1, -1):
            has_two_eq = nums[i] == nums[i + 1]
            has_three_eq = nums[i] == nums[i + 1] == nums[i + 2]
            has_three_incr = nums[i] + 1 == nums[i + 1] == nums[i + 2] - 1
            
            dp[i] = (has_two_eq and dp[i + 2]) or ((has_three_eq or has_three_incr) and dp[i + 3])

        return dp[0]
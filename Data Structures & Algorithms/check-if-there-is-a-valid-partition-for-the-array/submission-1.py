from functools import cache

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)

        dp: list[int] = [False for _ in range(n + 2)]
        dp[n] = True

        for i in range(n-1, -1, -1):
            has_two_eq = nums[i] == nums[i+1] if i + 1 < n else False
            has_three_eq = nums[i] == nums[i+1] and nums[i+1] == nums[i+2] if i + 2 < n else False
            has_three_incr = nums[i] + 1 == nums[i+1] and nums[i+1] + 1 == nums[i+2] if i + 2 < n else False
            
            ans = False

            if has_two_eq:
                ans = ans or dp[i + 2]
            
            if has_three_eq or has_three_incr:
                ans = ans or dp[i + 3]

            dp[i] = ans

        return dp[0]
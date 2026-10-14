class Solution:
    def rob(self, nums: List[int]) -> int:
        memo: list[list[int]] = [[0] * (len(nums) + 3) for _ in range(2)]

        for started_at_zero in range(2):
            for idx in range(len(nums) - 1, -1, -1):
                op1 = memo[started_at_zero][idx + 2] if not (started_at_zero and idx + 2 == len(nums) - 1) else 0
                
                op2 = memo[started_at_zero][idx + 3] if not (started_at_zero and idx + 3 == len(nums) - 1) else 0

                memo[started_at_zero][idx] = nums[idx] + max(op1, op2)

        return max(memo[True][0], memo[False][1], memo[False][2])

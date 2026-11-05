class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        modulus: dict[int, int] = {0: -1}
        if len(nums) < 2:
            return False

        running_sum = 0

        for i, num in enumerate(nums):
            running_sum += num
            cur_mod = running_sum % k
            if cur_mod in modulus and i - modulus[cur_mod] >= 2:
                return True
            if cur_mod not in modulus:
                modulus[cur_mod] = i

        return False
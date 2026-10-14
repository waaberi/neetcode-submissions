class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = sum(nums)
        ns = sum(range(len(nums) + 1))

        #print(s, ns)

        return ns - s
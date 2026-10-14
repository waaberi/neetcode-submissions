class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import defaultdict

        counter = defaultdict(int)

        for elem in nums:
            counter[elem] += 1
            if counter[elem] > 1: return True

        return False
         
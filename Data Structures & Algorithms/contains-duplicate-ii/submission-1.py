class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        counter = defaultdict(int)
        window = k+1
        for i in range(min(window, len(nums))):
            if counter[nums[i]] > 0:
                return True
            counter[nums[i]] += 1
        for i in range(window, len(nums)):
            counter[nums[i-window]] -= 1
            if counter[nums[i]] > 0:
                return True
            counter[nums[i]] += 1
        return False
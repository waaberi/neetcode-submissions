class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        members: set[int] = set()
        window = k+1
        for i in range(min(window, len(nums))):
            if nums[i] in members:
                return True
            members.add(nums[i])
        for i in range(window, len(nums)):
            members.remove(nums[i-window])
            if nums[i] in members:
                return True
            members.add(nums[i])
        return False
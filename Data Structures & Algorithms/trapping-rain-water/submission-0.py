class Solution:
    def trap(self, height: list[int]) -> int:
        left, right = 0, len(height)-1
        left_max = right_max = float('-inf')
        total = 0

        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if left_max < right_max: # bounded by left
                total += left_max-height[left]
                left += 1 # move right
            else: # bounded by right (or could be equal)
                total += right_max-height[right]
                right -= 1 # move left, also the direction doesnt matter in case of equality, you just need to make sure the program does not get stuck

        return total

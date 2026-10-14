"""
left = 0
right = 13
choice = 6
left = 0
right = 5
choice = 2
left = 3
right = 5
choice = 4
left = 3
right = 3
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0 # 3
        right = x # 5
        while left <= right:
            choice = (left + right) // 2
            sol = choice * choice
            if sol == x:
                return choice
            elif sol < x:
                left = choice + 1
            else: # my guess is too high
                right = choice - 1
        return left if left * left < x else left - 1 # idk
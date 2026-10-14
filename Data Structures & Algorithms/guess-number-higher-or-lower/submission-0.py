# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            choice = (left + right) // 2
            sol = guess(choice)
            if sol == 0:
                return choice
            elif sol == 1: # my guess is too low
                left = choice + 1
            else: # my guess is too high
                right = choice - 1
        return left # idk
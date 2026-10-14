class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        first_error = True
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                opt1 = s[left+1:right+1]
                opt2 = s[left:right]
                return opt1 == opt1[::-1] or opt2 == opt2[::-1]
        return True
        
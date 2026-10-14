class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [0] + digits
        digits[-1] += 1
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] > 9:
                digits[i] -= 10
                digits[i-1] += 1
        if digits[0]:
            return digits
        return digits[1:]
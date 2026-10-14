class Solution:
    def hammingWeight(self, n: int) -> int:
        s = 0
        while n != 0:
            s += n & 1
            n >>= 1
        return s
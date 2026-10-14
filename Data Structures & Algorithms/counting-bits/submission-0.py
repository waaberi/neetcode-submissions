"""
say n is 100101
is there something we can know about the amount of 1's in the number before it?
well in this case rn its 3 then itll be 2
but after that itll still be 2

ok i think the recommended time complexity listed is wrong just like last time so no need to overthink this i can copy my prev solution
"""

def hammingWeight(n: int) -> int:
    s = 0
    while n != 0:
        s += n & 1
        n >>= 1
    return s

class Solution:
    def countBits(self, n: int) -> List[int]:
        return [hammingWeight(i) for i in range(n+1)]
from math import sqrt, floor

class Solution:
    def arrangeCoins(self, n: int) -> int:
        # this is actually a constnat time problem LOL
        """
        just for the memes, lemme solve this in constant time
        so te formula for 1 + 2 + ... + n is n(n+1)//2

        actually lemme solve it legit before doing this

        x(x+1)//2 = n
        x*(x + 1) = 2n
        x^2 - x - 2n = 0

        a = 1
        b = -1
        c = -2n


        """

        return floor(sqrt(1 + 8 * n) - 1) // 2
        
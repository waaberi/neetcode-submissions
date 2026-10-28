class Solution:
    def arrangeCoins(self, n: int) -> int:
        # this is actually a constnat time problem LOL
        """
        just for the memes, lemme solve this in constant time
        so te formula for 1 + 2 + ... + n is n(n+1)//2

        actually lemme solve it legit before doing this
        """

        cur = 1
        while n >= cur:
            #print(n, cur)
            n -= cur
            cur += 1
        return cur - 1
        
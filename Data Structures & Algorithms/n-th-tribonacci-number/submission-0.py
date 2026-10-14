class Solution:
    def tribonacci(self, n: int) -> int:
        trib = [0, 1, 1]
        if n < 3:
            return trib[n]


        # do stuff

        # compute the last sum:  tmp = sum(trib)
        # trib[0] = trib[1]
        # trib[1] = trib[2]
        # trib[2] = tmp

        for _ in range(n - 2):
            tmp = sum(trib)
            trib[0] = trib[1]
            trib[1] = trib[2]
            trib[2] = tmp

        return trib[2]
class Solution:
    def climbStairs(self, n: int) -> int:
        mem2: list[int] = [0, 1, 0]

        for idx in range(n-1, -1, -1):
            mem2[0] = mem2[1] + mem2[2]
            mem2[2] = mem2[1]
            mem2[1] = mem2[0]

        return mem2[0]
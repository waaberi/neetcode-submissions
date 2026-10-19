class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """
        we're given an int and we need to generate the spiral
        and just give the thing as a result....
        i wanna figure out if there's a way to compute in O(1) per cell
        im just gonna do the manual mortion NGL
        """

        max_n = n**2

        arr = [[0 for _ in range(n)] for _ in range(n)]

        num = 1
        i = 0
        j = 0

        diagonal = 0
        cur_dir = 0

        while num <= max_n:
            arr[i][j] = num
            num += 1
            # then move i and j according to basic rules
            if cur_dir == 0:
                j = min(j + 1, n - diagonal - 1)
                if j == n - diagonal - 1:
                    cur_dir = 1
            elif cur_dir == 1:
                i = min(i + 1, n - diagonal - 1)
                if i == n - diagonal - 1:
                    cur_dir = 2
            elif cur_dir == 2:
                j = max(diagonal, j - 1)
                if j == diagonal:
                    cur_dir = 3
            elif cur_dir == 3:
                if (i-1, j) == (diagonal, diagonal):
                    cur_dir = 0
                    diagonal += 1
                    i = diagonal
                    j = diagonal
                else:
                    i = max(diagonal, i - 1)

        return arr
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        arr = [[0 for _ in range(n)] for _ in range(n)]

        num = 1
        diagonal = 0

        while diagonal < n:

            """
            start from (diagonal, diagonal)
            go all the way to the right
            go all the way down (don't double on top right)
            go all the way left (don't double on bottom right)
            go all the way up (don't double (diagonal, diagonal))
            update diagonal and reset.....
            """

            for j in range(diagonal, n - diagonal):
                arr[diagonal][j] = num
                num += 1
                #print(diagonal, j)

            for i in range(diagonal + 1, n - diagonal):
                arr[i][n - diagonal - 1] = num
                num += 1
                #print(i, n - diagonal - 1)
            
            for j in range(n - diagonal - 1 - 1, diagonal - 1, -1):
                arr[n - diagonal - 1][j] = num
                num += 1
                #print(n - diagonal - 1, j)

            for i in range(n - diagonal - 1 - 1, diagonal, -1):
                arr[i][diagonal] = num
                num += 1
                #print(i, diagonal)

            diagonal += 1

        return arr
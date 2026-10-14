"""
[0, 0] becomes [0, n - 1]
[0, 1] becomes [1, n - 1]
[0, n-1] becomes [n - 1, n - 1]
[2, 1] becomes [1, (n - 1) - 2]

ok so what is clear is:

(x, y) -> (y, n - 1 - x)
"""


from math import ceil

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for layer in range(ceil(n / 2)): # 0 is the shell, -1 is the kernel
            # figure out point from which we start the rotation process
            # inner loop until we get back to that point
            # go back to outer loop (which we're always in)
            # actually we'll do it for multiple points potentially, so we will have 3 loops
            # but not to worry, it's still O(n^2), bc each inner loop will actually be O(sqrt(n))
            """
            so the initial points we will just put them along the i axis. t's 0 to (n // 2) inclusive
            this is our i for loop

            now we need our rotation loop, ill keep it a while true until we figure something out
            """

            for i in range(n // 2):
                cur_i = i
                cur_j = layer

                tmp = matrix[cur_i][cur_j]

                started = False

                while not (started and cur_i == i and cur_j == layer): # rotation loop
                    started = True
                    new_i = cur_j
                    new_j = n - 1 - cur_i
                    #print(f"changing [{cur_i}][{cur_j}] into [{new_i}][{new_j}]")

                    new_val = matrix[new_i][new_j]
                    matrix[new_i][new_j] = tmp
                    tmp = new_val
                    cur_i = new_i
                    cur_j = new_j
                #print("done with that rotation")
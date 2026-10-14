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
        for layer in range(ceil(n / 2)):
            for i in range(n // 2):
                cur_i = i
                cur_j = layer

                tmp = matrix[cur_i][cur_j]

                new_i = cur_j
                new_j = n - 1 - cur_i
                new_val = matrix[new_i][new_j]
                matrix[new_i][new_j] = tmp
                tmp = new_val
                cur_i = new_i
                cur_j = new_j

                while not (cur_i == i and cur_j == layer): # rotation loop
                    started = True
                    new_i = cur_j
                    new_j = n - 1 - cur_i
                    new_val = matrix[new_i][new_j]
                    matrix[new_i][new_j] = tmp
                    tmp = new_val
                    cur_i = new_i
                    cur_j = new_j
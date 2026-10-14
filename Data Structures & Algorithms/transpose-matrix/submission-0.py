"""

"""


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        nm = [[0] * len(matrix) for _ in range(len(matrix[0]))]
        for j in range(len(matrix)):
            for i in range(len(matrix[0])):
                nm[i][j] = matrix[j][i]

        return nm
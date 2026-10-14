class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m * n - 1

        while left <= right:
            guess = (left + right) // 2
            i = guess // n
            j = guess % n
            num = matrix[i][j]
            if num == target:
                return True
            elif num > target:
                right = guess - 1
            else: # num > target
                left = guess + 1

        return False
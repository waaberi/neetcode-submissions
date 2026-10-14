class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        def one_to_two(x: int) -> tuple[int, int]:
            i = x // n
            j = x % n
            return i, j

        left = 0
        right = m * n - 1

        while left <= right:
            guess = (left + right) // 2
            i, j = one_to_two(guess)
            num = matrix[i][j]
            if num == target:
                return True
            elif num > target:
                right = guess - 1
            else: # num > target
                left = guess + 1

        return False
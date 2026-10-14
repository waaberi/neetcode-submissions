class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict

        square_counter = [defaultdict(int) for _ in range(9)]

        def pc(i, j): # for the square check
            return 3 * (i // 3) + j // 3

        column_counter = [defaultdict(int) for _ in range(9)]

        for i in range(9):
            # row check
            row_counter = defaultdict(int)
            for j in range(9):
                # column check
                if board[i][j] == ".": continue
                row_counter[board[i][j]] += 1
                column_counter[j][board[i][j]] += 1
                square_counter[pc(i, j)][board[i][j]] += 1
                if row_counter[board[i][j]] > 1:
                    print("Failed row check")
                    return False # row check
                if column_counter[j][board[i][j]] > 1:
                    print("Failed column check at", i, j)
                    print(column_counter)
                    return False # column check
                if square_counter[pc(i, j)][board[i][j]] > 1:
                    print("Failed square check")
                    return False # square check
        
        return True
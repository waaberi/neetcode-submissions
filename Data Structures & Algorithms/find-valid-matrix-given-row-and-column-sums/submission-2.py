class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows = len(rowSum)
        columns = len(colSum)
        matrix = [[0 for _ in range(columns)] for _ in range(rows)]
        """
        so the idea is to fill col 0 first
        then while its invalid shift some of the stuff to the next col greedily
        and just continue doing this till ur at the end
        and we're guaranteed a valid solution so this should work
        """

        for row in range(rows):
            matrix[row][0] = rowSum[row]
        
        for col in range(columns):
            # get the current sum
            # for each element greedily shift the difference to the right
            # continue
            col_sum = sum(matrix[x][col] for x in range(rows))
            target_sum = colSum[col]
            for row in range(rows):
                if col_sum == target_sum:
                    break
                deficit = col_sum - target_sum
                to_remove = min(deficit, matrix[row][col])
                matrix[row][col] -= to_remove
                # if this is valid there shouldn't be an error here so ill let it slide loool
                matrix[row][col + 1] += to_remove
                col_sum -= to_remove

        return matrix
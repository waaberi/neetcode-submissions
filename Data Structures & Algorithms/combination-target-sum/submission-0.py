class Solution:
    """
    we know tthis is a backtracking problem
    i will implement the following (or not lol):
    - is_valid_state (optional)
    - get_candidates (optional)
    - search (mandatory)
    - solve (combinationSum itself)

    acc i will do them inside of combinationSum since this is gonna be easier cuz i can reuse variables instead of passing them as params

    im always a bit confused about the role of is_valid_state vs get_candidates

    i will say that this is very similar to the subset problem where for each index we decide whether to take it or not

    i will structure my search function as such

    bruh i just realized u can use any num an unlimited amount  of times

    this can introduce a cycle, actually no there wont be a cycle because the sum being too large is an escape hatch

    """

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = []

        def search(sol: list[int], i: int):
            sol_sum = sum(sol)
            if sol_sum > target:
                return
            elif sol_sum == target:
                answer.append(sol.copy())
                return
            
            if i == len(nums):
                return

            sol.append(nums[i])
            search(sol, i)
            sol.pop()
            search(sol, i + 1)

        search([], 0)

        return answer
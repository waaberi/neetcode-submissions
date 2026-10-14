class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = []

        def search(sol: list[int], i: int, sol_sum: int):
            if sol_sum > target:
                return
            elif sol_sum == target:
                answer.append(sol.copy())
                return
            
            if i == len(nums):
                return

            sol.append(nums[i])
            search(sol, i, sol_sum + nums[i])
            sol.pop()
            search(sol, i + 1, sol_sum)

        search([], 0, 0)

        return answer
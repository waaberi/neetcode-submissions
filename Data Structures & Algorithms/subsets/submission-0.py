class Solution:
    def search(self, nums: list[int], cur_arr: list[int], i: int, solutions: list[list[int]]):
        if i == len(nums):
            solutions.append(cur_arr.copy())
            return
        cur_arr.append(nums[i])
        self.search(nums, cur_arr, i + 1, solutions)
        cur_arr.pop()
        self.search(nums, cur_arr, i + 1, solutions)

    def subsets(self, nums: list[int]) -> list[list[int]]:
        solutions = []

        self.search(nums, [], 0, solutions)

        return solutions
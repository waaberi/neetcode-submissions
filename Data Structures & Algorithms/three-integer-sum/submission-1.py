from collections import defaultdict

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # maybe do nested loop (i, j) and then use the complement approach
        # not sure how this is supposed to be o(1) space though. we'd need a dict so this is not gonna be o(1) since its size is somewhat correlated to the input although not linearly
        
        # i'm lazy i'll do the 2 pass approach and simplify later

        dat: dict[int, list[tuple[int, int]]] = defaultdict(list)

        output: set[tuple[int, int, int]] = set() # would've been better as a list[tuple[int, int, int]]

        for i in range(len(nums)):
            for j in range(len(nums)):
                complement = -(nums[i] + nums[j])
                dat[complement].append((i, j))


        for i in range(len(nums)):
            if nums[i] not in dat:
                continue

            for j, k in dat[nums[i]]:
                if i == j or i == k or j == k: # i thought check 3 would've been useless.... clearly im doing something wrong. also i think i should probably be using a defaultdict list and just appending.
                    continue

                output.add(tuple(sorted([nums[i], nums[j], nums[k]]))) # very little overhead hopefully! 



        # i'll just convert output before returning it, doesn't matter...
        return [list(i) for i in output]

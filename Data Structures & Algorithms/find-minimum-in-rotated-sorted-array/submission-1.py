class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        ok so we're being asked to find the minimum of a rotated array
        the nice thing about sorted arrays is that theres guarantted to be at most 1 adjacency where the element to the left is  bigger than the element ot the right (if not rotated, then index -1 is bigger than index 0, for example)
        so we just have to scan for these indexes. we can go check from index -1 to index n - 1 inclusive i guess? realistically its n - 2, so ill do that instead

        ok so something i need to think about before finishing the code is this:
        what to do when its NOT  the c ase? do i know which side to cut? if i dont know which side to cut it cannot be log.

        how about we do it slightly differently? first of all i want to rewrite the code such that we are looking at the right side numbern ot the left side. this avoids negatives.

        ok that part was easy to fix.

        now, could we not potentially just try determining the upper bound by multiplying? so say lower = 0 and upper = 0. we keep trying upper and we see if upper is greater. if it is greater, then we add 1 (later add 2, then 4, then 8, etc). evntually it'll get smaller, no?

        lets try writing the code for that and we'll see what happens. 

        btw ive reverted that change its easier to start at -1 and 0 because then it gets the default case (no rotation) sorted out really nicely while i still have the bandwidth to think about the other cases.

        """
        n = len(nums)

        left = 0
        right = n - 1
        while left < right:
            middle = (left + right) // 2
            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle

        return nums[left]

        
            
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        what we need to think about is to basically set a replacement index
        so for example, at i = 0 we can say the replacement index is also 0
        as long as theyre equal a swap does nothing but that doesnt matter we can jsut do it lol


        the key here is to figure out when the replacement index stops goign up
        so whenever we find a non-unique element we actually just stop increasing k i think?
        """
        k = 0
        prev_elem = -101
        for i, num in enumerate(nums):
            if num != prev_elem:
                nums[k] = nums[i]
                k += 1


            # do a bunch of stuff
            prev_elem = num
        return k
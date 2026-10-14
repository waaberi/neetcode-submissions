from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        assume we have a k
        how do we know its valid?
        you can traverse the entire array and count the amount of times it divides k, +1 if theres leftovers
        if thats less than or equal to h you're good

        that algorithm is O(N)
        so if we haave a lower bound and an upper bound we can do binary search on that to find the lowest valid, and it would be  O(log M) * O(N). i don tknow how large M is yet, need to find the upper bound.

        i wonder if we can compute a reasonable upper bound in O(1)

        to be fair, we don't really need to. we can use binary search for that too.
        """

        def is_k_valid(k: int) -> bool:
            total_hours = 0
            for banana_count in piles:
                total_hours += banana_count // k + (banana_count % k > 0)
            return total_hours <= h

        lower = 1
        upper = 1
        while not is_k_valid(upper):
            lower = upper
            upper *= 2

        record = float('inf')

        while lower <= upper:
            new_k = (lower + upper) // 2
            if is_k_valid(new_k):
                upper = new_k - 1
                record = min(record, new_k)
            else:
                lower = new_k + 1

        return record
        
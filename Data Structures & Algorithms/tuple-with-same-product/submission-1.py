class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        """
        10^3

        so this could totally allow for n^2
        one thing i wanna figure out here is
        the tuples just have to be distinct right.....
        so their ordering doesnt RLY Matter
        once u identify the 4 tuples you alr know theres 8 possibilities
        they did that math fro us

        so i propose that we sort it

        and then we deal with it somehow

        what we want to do is to figure out for each valid pair what the product is....

        theres gonna be n^2 / 2 unique pairs it is ok to store them all i think

        we're gonna make a dict that contains those
        thne do some basic combinatorics on that
        lwk if i do this why do i need to sort in the first place?
        dont think i do for now

        so ill do that lol
        """

        n = len(nums)
        prod_dict: dict[int, list[tuple[int, int]]] = defaultdict(int)

        answer = 0

        for i in range(n-1):
            for j in range(i + 1, n):
                num_i = nums[i]
                num_j = nums[j]
                prod_dict[num_i * num_j] += 1
            

        for product in prod_dict:
            pair_count = prod_dict[product]
            if pair_count < 2:
                continue
            answer += (pair_count * (pair_count - 1) // 2) * 8


        return answer

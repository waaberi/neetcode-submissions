class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        from operator import itemgetter

        counter = defaultdict(int)

        for elem in nums: counter[elem] += 1

        return [
            key for key, value in 
            sorted(counter.items(), key=itemgetter(1), reverse=True)[:k]
        ]
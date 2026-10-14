class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        store = defaultdict(list)

        def assign_score(s: str) -> str:
            return str(sorted(s))

        for s in strs:
            store[assign_score(s)].append(s)

        return [store[score] for score in store]

        
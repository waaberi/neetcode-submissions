class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """
        town judge trusts nobody
        everybody trusts the town judge
        there is someone who satisfies both


        trust where trust[i] = [ai, bi] which means that ai trusts bi

        return towwn judge id if possible, otherwise return -11
        """

        trusted_by: dict[int, set[int]] = defaultdict(set)
        trusts: dict[int, set[int]] = defaultdict(set)

        people: set[int] = set()

        for ai, bi in trust:
            trusts[ai].add(bi) # ai trusts bi
            trusted_by[bi].add(ai) # bi is trusted by ai
            people.add(ai)
            people.add(bi)

        for person in people:
            if trusts[person]:
                continue
            if len(trusted_by[person]) != (len(people) - 1):
                continue
            return person

        return -1
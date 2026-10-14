"""
trying to see if i can create a list of who to look into to speed up the process
otherwise i dont mind looping through everyone
ig ill loop through everyone first and then figure things oout later
"""

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        a_trusts_b: dict[int, set[int]] = defaultdict(set[int])
        b_is_trusted_by_a: dict[int, set[int]] = defaultdict(set[int])

        for a, b in trust:
            a_trusts_b[a].add(b)
            #a_trusts_b[b] # register in the dict
            b_is_trusted_by_a[b].add(a)
            #b_is_trusted_by_a[a] # register in the dict

        for b in b_is_trusted_by_a:
            if not a_trusts_b[b]:
                #print("potential candidate", b)
                #print(b_is_trusted_by_a[b], a_trusts_b.keys())
                if b_is_trusted_by_a[b] | {b} == a_trusts_b.keys():
                    return b
            
        return -1

        
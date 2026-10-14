from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1 = Counter(s)
        c2 = Counter(t)

        for e in c1:
            if c2[e] != c1[e]:
                return False
        
        # we've confirmed everything in c1 is in c2
        # therefore a length check should be enough
        return len(c1) == len(c2)
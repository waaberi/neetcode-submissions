class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict

        counter_s = defaultdict(int)
        counter_t = defaultdict(int)

        if len(s) != len(t): return False

        for i in range(len(s)):
            counter_s[s[i]] += 1
            counter_t[t[i]] += 1

        for letter in counter_s:
            if counter_s[letter] != counter_t[letter]: return False

        return True
        
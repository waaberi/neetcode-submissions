class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        lst = ""
        for i in range(min(len(word1), len(word2))):
            lst += word1[i]
            lst += word2[i]
        for j in range(i+1, len(word1)):
            lst += word1[j]
        for j in range(i+1, len(word2)):
            lst += word2[j]
        return lst
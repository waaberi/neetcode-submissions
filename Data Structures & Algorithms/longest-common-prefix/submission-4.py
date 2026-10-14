class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if len(strs[j]) <= i or strs[j][i] != strs[j-1][i]:
                    return strs[j][:i]

        return strs[0]
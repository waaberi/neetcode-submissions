from functools import cache

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp: list[list[int]] = [[0 for _ in range(27)] for _ in range(len(s) + 1)]

        def idx_to_letter(i: int) -> str:
            return "" if i == 0 else chr(i - 1 + ord('a'))
        
        def letter_to_idx(ch: str) -> int:
            return (ord(ch) - ord('a') + 1) if ch else 0

        for cur_i in range(len(s) - 1, -1, -1):
            for letter_idx in range(27):
                last_ch = idx_to_letter(letter_idx)
                
                skip = dp[cur_i+1][letter_idx]
                can_take = not last_ch or abs(ord(s[cur_i]) - ord(last_ch)) <= k
                if can_take:
                    take = 1 + dp[cur_i + 1][letter_to_idx(s[cur_i])]
                    dp[cur_i][letter_idx] = max(take, skip)
                else:
                    dp[cur_i][letter_idx] = skip


        return dp[0][0]
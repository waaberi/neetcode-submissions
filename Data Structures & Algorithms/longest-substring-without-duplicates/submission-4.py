class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_occurances: dict[str, int] = {}
        maximum_length = 0
        window_start = 0
        for i, ch in enumerate(s):
            if ch in last_occurances:
                window_start = max(window_start, last_occurances[ch] + 1)

            last_occurances[ch] = i
            maximum_length = max(maximum_length, i - window_start + 1)

        return maximum_length


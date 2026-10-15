class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_occurances: dict[str, int] = {}
        maximum_length = 0
        current_length = 0
        window_start = 0
        for i, ch in enumerate(s):
            if ch in last_occurances:
                window_start = max(window_start, last_occurances[ch] + 1)

            last_occurances[ch] = i
            current_length += 1
            maximum_length = max(maximum_length, current_length - window_start)

        return maximum_length


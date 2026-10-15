class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_occurances: dict[str, int] = {}
        maximum_length = 0
        previous_cut = -1
        current_length = 0
        for i, ch in enumerate(s):
            if ch in last_occurances and last_occurances[ch] > previous_cut:
                previous_occurance = last_occurances[ch]
                current_length -= (previous_occurance - previous_cut)
                previous_cut = previous_occurance

            last_occurances[ch] = i
            current_length += 1
            maximum_length = max(maximum_length, current_length)

        return maximum_length


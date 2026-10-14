class Solution:
    def romanToInt(self, s: str) -> int:
        ptr = 0
        symval: dict[str, int] = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        val = 0

        while ptr < len(s) - 1:
            cur = symval[s[ptr]]
            _next = symval[s[ptr + 1]]
            if cur < _next:
                val += _next - cur
                ptr += 1
            else:
                val += cur
            
            ptr += 1

        if ptr == len(s) - 1:
            val += symval[s[ptr]]

        return val

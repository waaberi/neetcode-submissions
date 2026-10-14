def full_adder(a: int, b: int, c_in: int) -> tuple[int, int]: # s, c_out
    s = a ^ b ^ c_in
    c_out = a&b | b&c_in | c_in&a
    return s, c_out
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c_in = 0
        ans = []
        if len(b) > len(a):
            a, b = b, a
        b = "0" * (len(a) - len(b)) + b

        for i in range(len(a)):
            s, c_in = full_adder(int(a[-(i + 1)]), int(b[-(i + 1)]), c_in)
            ans.append(s)
        if c_in:
            ans.append(c_in)
        return "".join(str(i) for i in reversed(ans))
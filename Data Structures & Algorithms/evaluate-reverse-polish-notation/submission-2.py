def stupid_div(a, b):
    if a >= 0 and b >= 0:
        return a // b
    if a < 0 and b < 0:
        return abs(a) // abs(b)
    return -(abs(a) // abs(b))


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.isdigit() or (token[0] == "-" and token[1:].isdigit()):
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else: # token == "/" /
                    stack.append(stupid_div(a, b))

        return stack[0]
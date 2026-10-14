class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        s = 0
        for op in operations:
            if op == "+":
                tmp = record[-1] + record[-2]
                s += tmp
                record.append(tmp)
            elif op == "D":
                tmp = record[-1] * 2
                record.append(tmp)
                s += tmp
            elif op == "C":
                s -= record.pop()
            else: # number
                tmp = int(op)
                record.append(tmp)
                s += tmp
        return s
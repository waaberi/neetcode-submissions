"""
A-Z = 26 (coef is 1-26, base is 0, exp is 26)
then there's 26*26 more things like that (coef is 1-26, base is 1, exp is 26)
then there's 26*26*26 more things like that (coef is 1-26, base is 2, exp is 26)
etc

"""

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        """
        imagine this as being base 26
        """
        arr = []
        ans = ""

        for exp in range(6, -1, -1):
            for coef in range(26, 0, -1):
                # Check if current value can be subtracted while leaving at least 1 for each smaller position
                # The minimum value for remaining digits is (26 ** exp - 1) // 25
                remaining_min = (26 ** exp - 1) // 25
                if columnNumber - (coef * 26 ** exp) >= remaining_min:
                    arr.append((exp, coef))
                    ans += chr(ord("A") + coef - 1)
                    columnNumber -= coef * 26 ** exp
                    break
        
        print(arr)

        return ans

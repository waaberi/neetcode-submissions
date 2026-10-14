"""

NANANA


i have a ptr thats salways at 0
0: 0, 1, 3 0:3

AANAAN
"""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        for i in range(min(len(str1), len(str2))):
            if str1[i] != str2[i]:
                return ""

        sep = 0

        for i in range(1, 1 + min(len(str1), len(str2))):
            print(i)
            if i < len(str1) and str1[i] != str1[0]:
                continue

            if len(str1) % i != 0:
                continue

            if len(str2) % i != 0:
                continue
            #print("this is a serious candidate", i)

            for j in range(i, len(str1)):
                if str1[j] != str1[j - i]:
                    #print("mismatch at str1")
                    break
            else:
                for j in range(i, len(str2)):
                    if str2[j] != str2[j - i]:
                        #print("mismatch at str2")
                        break
                else:
                    sep = i
            


        return str1[:sep]
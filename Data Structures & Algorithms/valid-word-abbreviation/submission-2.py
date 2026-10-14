"""
IM OVERCOMPLICATING THIS
WHEN A NUMBER IS FINISHED, I JUMP BY THAT NUMBER FROM THE INDEX IT APPEARED AT
OTHERWISE, I JUMP BY 1
NO MATTER WHAT, I COMPARE THE 2 POINTERS TO SEE IF THEYRE EQUAL IN VALUE IF POSSIBLE
THEN AT THE END I DO ONE LAST CHECK THIS ONE ILL LOOK INTO LATER
"""

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        wp = 0
        store = 0 # going to contain the potential numbers
        num_jump = 0
        for ap in range(len(abbr)):
            if abbr[ap].isalpha():
                if num_jump:
                    wp = wp - num_jump + store
                    num_jump = 0
                    store = 0
                if wp < len(word) and abbr[ap] != word[wp]:
                    return False
            else:
                if num_jump == 0 and abbr[ap] == "0":
                    return False
                store *= 10
                store += int(abbr[ap])
                num_jump += 1
            wp += 1

        if num_jump:
            wp = wp - num_jump + store
        return wp == len(word)
        


            
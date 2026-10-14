class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
        
        for bill in bills:
            change = bill - 5

            if bill == 10:
                tens += 1
            elif bill == 5:
                fives += 1

            while change > 0:
                if change > 10 and tens > 0:
                    tens -= 1
                    change -= 10
                elif change >= 5 and fives > 0:
                    fives -= 1
                    change -= 5
                else:
                    return False
            

        return True
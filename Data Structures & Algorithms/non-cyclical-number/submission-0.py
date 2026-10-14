class Solution:
    def isHappy(self, n: int) -> bool:
        store: set[int] = set([n])
        while True:
            n = sum(int(i)**2 for i in str(n))
            if n == 1:
                return True
            if n in store:
                return False
            store.add(n)


        return False
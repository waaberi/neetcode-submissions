import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        """
        is is happy if:
        - only has a, b, and c
        - does not have "aaa", "bbb", "ccc"
        - max a occurances of "a"
        - max b occurances of "b"
        - max c occurances of "c"


        this is a sliding window problem



        ill need to figure out what to od when adding to the sliding window and when removing


        what i will do is i will push it right and then if theres any failure then i move left ptr right too......


        ookkkkk i misunderstrood the problem


        i create the string myself


        ok well basically a, b, and c are budgets


        and i think i should probably try alternating them until it possibly stops working..


        for example:


            abcabcabcabc

        b = 2
        c = 5

        ccbcbcc

        max-heap i think

        i need to know at any time what i have the best budget for


        for example for a = 3, b = 4, c = 2

        i have a high budget for b

        i spend basically

        a = 3, b = 3, c = 2
        s = "b"

        whenever equal i pick something idfferent


        a = 2, b = 3, c = 2
        s = "ba"

        
        now we're back to b

        a = 2, b = 2, c = 2
        s = "bab"

        ok but my strat is a bit different, does it rly matter what i pick for greedy other than it not being b?

        no idea TBH.....

        but also then i sgtruggle to see why a min heap matters here


        oh and also i cant pick the same thing 3 times in a row


        but then i still dont see why id need a heap TBH

        theres only 3 vars to keep track of no?

        but ig the heap makes them easy to manage so i actually dont even mind
        """

        arr = []

        if a:
            arr.append((-a, 'a'))
        if b:
            arr.append((-b, 'b'))
        if c:
            arr.append((-c, 'c'))

        heapq.heapify(arr)

        s = ""

        held = None

        consecutive = [0, 0, 0]
        let_to_idx: dict[str, int] = {"a": 0, "b": 1, "c": 2}
        while arr:
            count, letter = heapq.heappop(arr)
            count = -count
            idx = let_to_idx[letter]
            if consecutive[idx] >= 2: # we are in trouble
                if not arr:
                    continue
                held = (-count, letter)
                count, letter = heapq.heappop(arr)
                count = -count
                idx = let_to_idx[letter]

            for i in range(len(consecutive)):
                if i != idx:
                    consecutive[i] = 0
                else:
                    consecutive[i] += 1
            s += letter
            count -= 1
            if count > 0:
                heapq.heappush(arr, (-count, letter))
            if held is not None:
                heapq.heappush(arr, held)
                held = None

        return s




class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        result: list[int] = [0] * len(temperatures)

        # i hate monotonic stacks

        s = [(0, temperatures[0])]
        """
        lets keep everything smaller
        the new question to answer is, for the current element im mlooking at are there past solution?

        we'll figure out what exactly to store in the stack later. probably a tuple of day and idx. 
        """

        for i in range(1, len(temperatures)):
            temp = temperatures[i]

            while len(s) and temp > s[-1][1]:
                old_i, _ = s.pop()
                result[old_i] = i - old_i

            s.append((i, temp))


        return result
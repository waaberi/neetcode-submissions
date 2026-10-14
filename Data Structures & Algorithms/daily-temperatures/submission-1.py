class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        result: list[int] = [0] * len(temperatures)

        # i hate monotonic stacks

        temp_stack = []
        """
        lets keep everything smaller
        the new question to answer is, for the current element im mlooking at are there past solution?

        we'll figure out what exactly to store in the stack later. probably a tuple of day and idx. 
        """

        for i, cur_temp in enumerate(temperatures):
            while temp_stack and cur_temp > temperatures[temp_stack[-1]]:
                old_i = temp_stack.pop()
                result[old_i] = i - old_i

            temp_stack.append(i)


        return result
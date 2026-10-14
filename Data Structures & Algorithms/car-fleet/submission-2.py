class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        i watched the video about that though i didnt see the code
        i think for this the first step is to sort since there is a constraint that the cars must stay in a specific order and that order is their current pos. so if we sort it'll be easier to maintain such an order cuz we can do it in one direction

        unfortunately it is currently 2 different arrays so my solution is to combine them first and then sort
        """

        arr = []
        for i in range(len(position)):
            hours_left = (target - position[i]) / speed[i]
            arr.append([position[i], speed[i], hours_left])

        arr.sort(key=lambda x: -x[0])

        # ok its sorted now

        # after that, the basic idea is the following
        # if a car to the right ever meets the car to the left, it will be grouped with the car to the left

        """
        oh wait theres a detail  i forgot
        in the solution he wants to make the computation a lot easier by calculating the amount of hours left
        because once thats calcualted then simply hacving <= hours left than the element ot the left guarantees that they will evnetually meet
        """

        count = 1

        #print(arr)

        
        for i in range(1, len(arr)):
            if arr[i][2] <= arr[i-1][2]:
                # my guess is we may have to modify hours left
                # can't we just make it equal to the same as the previous one just in case?
                # will remove if not useful
                arr[i][2] = arr[i-1][2]
            else:
                count += 1


       # print(arr)

        return count
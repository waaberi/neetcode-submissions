class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        """
        1. ignore everyone at the limit or above
        say that 0 to n-1 inclusive is below the limit
        [2, 2, 3, 4, 5, 9], limit = 10
        """
        left = 0
        right = len(people) - 1
        while left <= right:
            guess = (left + right) // 2
            if people[guess] < limit:
                left = guess + 1
            else:
                right = guess - 1
        
        # range(left) corresponds to all indexes below the limit, or range(right+1)

        left = 0 # we keep right, we'll do 2 pointer again

        optimum = len(people)
        #print(left, right, people[left] + people[right])
        while left < right:
            if people[left] + people[right] <= limit:
                optimum -= 1
                left += 1
                right -= 1
            else:
                right -= 1
            #print(left, right, people[left] + people[right])

        return optimum

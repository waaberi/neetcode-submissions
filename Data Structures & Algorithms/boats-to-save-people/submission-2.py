class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1
        while left <= right:
            guess = (left + right) // 2
            if people[guess] < limit:
                left = guess + 1
            else:
                right = guess - 1

        left = 0 # we keep right, we'll do 2 pointer again

        optimum = len(people)
        while left < right:
            if people[left] + people[right] <= limit:
                optimum -= 1
                left += 1
            right -= 1

        return optimum

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []
        for i in range(len(position)):
            hours_left = (target - position[i]) / speed[i]
            arr.append([position[i], hours_left])

        arr.sort(key=lambda x: x[0], reverse=True)

        count = 0
        
        time_at_fleet_creation = 0

        for i in range(len(arr)):
            if arr[i][1] > time_at_fleet_creation:
                time_at_fleet_creation = arr[i][1]
                count += 1

        return count
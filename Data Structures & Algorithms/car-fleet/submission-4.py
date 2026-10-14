class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []
        for i in range(len(position)):
            hours_left = (target - position[i]) / speed[i]
            arr.append([position[i], hours_left])

        arr.sort(key=lambda x: -x[0])

        count = 1
        
        for i in range(1, len(arr)):
            if arr[i][1] <= arr[i-1][1]:
                arr[i][1] = arr[i-1][1]
                pass
            else:
                count += 1

        return count
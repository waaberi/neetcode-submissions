class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        max_area = 0
        for new_pos, new_height in enumerate(heights):
            old_pos = new_pos
            while stack and stack[-1][1] > new_height:
                old_pos, old_height = stack.pop()
                max_area = max(max_area, (new_pos - old_pos) * old_height)
            stack.append((old_pos, new_height))

        while stack:
            old_pos, old_height = stack.pop()
            max_area = max(max_area, (n - old_pos) * old_height)

        return max_area
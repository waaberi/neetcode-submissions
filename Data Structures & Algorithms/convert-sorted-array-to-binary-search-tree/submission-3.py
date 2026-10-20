from collections import deque


"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


depth first search


def 
"""

def dfs(nums: list[int], left: int, right: int) -> Optional[TreeNode]:
    if left > right:
        return None

    middle = (left + right) // 2
    node = TreeNode(nums[middle], None, None)

    left = dfs(nums, left, middle - 1)
    right = dfs(nums, middle + 1, right)
    node.left = left
    node.right = right

    return node

    

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return dfs(nums, 0, len(nums) - 1)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # this solution is O(N^2)
        def depth(node: Optional[TreeNode]):
            if node is None:
                return 0
            return 1 + max(depth(node.left), depth(node.right))

        if root is None:
            return True

        if abs(depth(root.left) - depth(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
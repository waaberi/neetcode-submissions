# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def depth(node: Optional[TreeNode]):
            nonlocal max_diameter
            if node is None:
                return 0

            left_depth = depth(node.left)
            right_depth = depth(node.right)

            max_diameter = max(max_diameter, left_depth + right_depth)

            return 1 + max(left_depth, right_depth)

        depth(root) # compute the depth

        return max_diameter
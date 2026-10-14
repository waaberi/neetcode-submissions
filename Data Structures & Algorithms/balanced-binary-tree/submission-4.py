# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced = True


        def depth(node: Optional[TreeNode]):
            nonlocal is_balanced
            if not is_balanced: # don't waste time
                return 0 # doesn't rly matter what we return the result is garbage

            if node is None:
                return 0

            depth_left = depth(node.left)
            depth_right = depth(node.right)

            if is_balanced:
                is_balanced = abs(depth_left - depth_right) <= 1

            return 1 + max(depth_left, depth_right)

        depth(root)

        return is_balanced
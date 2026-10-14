# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # this solution is O(N^2)
        # we can do O(N), i just need to think about it more.
        """
        im inspired by the diameter problem, where we calculate the diameter as we calculate the depth
        when we calculate the depth we are also able to calculate balanced at the same time, i dont see why not.

        we have the depth of the left, and the depth of the rgith. thats all we need


        """

        is_balanced = True


        def depth(node: Optional[TreeNode]):
            nonlocal is_balanced
            if not is_balanced: # don't waste time
                return 0 # doesn't rly matter what we return the result is garbage

            if node is None:
                return 0

            depth_left = depth(node.left)
            depth_right = depth(node.right)

            is_balanced = abs(depth_left - depth_right) <= 1

            return 1 + max(depth(node.left), depth(node.right))

        depth(root)

        return is_balanced
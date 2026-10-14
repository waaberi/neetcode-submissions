# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        the diameter in general is just the depth of left + the depth of right
        """

        if root is None:
            return 0

        def depth(node: Optional[TreeNode]):
            if node is None:
                return 0

            return 1 + max(depth(node.left), depth(node.right))

        def diameter(node: Optional[TreeNode]):
            if node is None:
                return 0

            return depth(node.left) + depth(node.right)

        return max(diameter(root), self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
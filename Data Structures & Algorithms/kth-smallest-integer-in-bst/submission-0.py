# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        the idea of this is to do in-order traversal
        in-order traversal is left, middle, right
        """

        arr = []

        def inorder(node: Optional[TreeNode]):
            if len(arr) >= k:
                return
            if node is None:
                return
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)


        inorder(root)
        return arr[k-1]

        
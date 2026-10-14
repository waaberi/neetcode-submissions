# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def ivb(node: Optional[TreeNode] = root, min_val: int = float('-inf'), max_val: int = float('inf')):
            if node is None:
                return True

            if not min_val < node.val < max_val:
                return False

            return ivb(node.left, min_val, node.val) and ivb(node.right, node.val, max_val)
            
        return ivb()
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def getGoodNodes(node: TreeNode | None, max_value: int = -101):
            if node is None:
                return 0
                
            if node.val >= max_value:
                return 1 + getGoodNodes(node.left, node.val) + getGoodNodes(node.right, node.val)

            return getGoodNodes(node.left, max_value) + getGoodNodes(node.right, max_value)

        return getGoodNodes(root)
        
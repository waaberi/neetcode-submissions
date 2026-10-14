# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        stack: list[TreeNode] = [root]

        while stack:
            ptr = stack.pop()
            if p.val < ptr.val and q.val < ptr.val:
                stack.append(ptr.left)
            elif p.val > ptr.val and q.val > ptr.val:
                stack.append(ptr.right)
            else:
                return ptr
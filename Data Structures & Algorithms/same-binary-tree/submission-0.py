# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack: list[tuple[Optional[TreeNode], Optional[TreeNode]]] = [(p, q)]

        while stack:
            p_ptr, q_ptr = stack.pop()
            if p_ptr is None and q_ptr is None:
                continue
            if p_ptr is None or q_ptr is None or p_ptr.val != q_ptr.val:
                return False

            stack.append((p_ptr.left, q_ptr.left))
            stack.append((p_ptr.right, q_ptr.right))

        return True

        
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue: deque[tuple[int, Optional[TreeNode]]] = deque([(0, root)])
        answer = []
        while queue:
            depth, node = queue.popleft()
            if node is None:
                continue
            if len(answer) == depth:
                answer.append([node.val])
            else:
                answer[depth].append(node.val)
            queue.append((depth + 1, node.left))
            queue.append((depth + 1, node.right))
        return answer
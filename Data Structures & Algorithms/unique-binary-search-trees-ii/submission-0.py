from collections import deque, defaultdict
import copy

class Solution:
    def generateTrees(self, n: int) -> list[TreeNode]:
        ids: dict[tuple[TreeNode, int, int] | None, int] = defaultdict(lambda: len(ids))
        ids[None]

        def get_id(node: TreeNode | None) -> int:
            if node in ids:
                return ids[node]
            tup = (node.val, get_id(node.left), get_id(node.right))
            return ids[tup]



        final_answer: list[TreeNode] = []
        queue: deque[tuple[TreeNode, list[int]]] = deque([(TreeNode(x), [option for option in range(1, n+1) if option != x]) for x in range(1, n+1)])
        set_ids: set[int] = set()

        def try_place(node: TreeNode, val: int):
            if node.left and val < node.val:
                return try_place(node.left, val)
            
            if node.right and val > node.val:
                return try_place(node.right, val)

            if val > node.val:
                node.right = TreeNode(val)
            else:
                node.left = TreeNode(val)


        while queue:
            root, options = queue.popleft()
            if not options:
                root_id = get_id(root)
                if root_id not in set_ids:
                    final_answer.append(root)
                    set_ids.add(root_id)
            
            for option in options:
                node = copy.deepcopy(root)
                try_place(node, option)
                new_options = [new_option for new_option in options if option != new_option]
                queue.append((node, new_options))


        return final_answer
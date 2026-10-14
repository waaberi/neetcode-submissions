# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # some cursed defaultdict slop
        root_dict: dict[tuple[int, int, int], int] = defaultdict(lambda: len(root_dict) + 1)

        def get_id(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            left_id = get_id(node.left)
            right_id = get_id(node.right)

            tup = (node.val, left_id, right_id)

            return root_dict[tup] # it will create a new id if one does not exist already

        get_id(root)

        dict_size = len(root_dict)

        return get_id(subRoot) <= dict_size
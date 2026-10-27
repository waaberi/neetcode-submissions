# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        ptr = head
        while ptr:
            arr.append(ptr)
            ptr = ptr.next

        # this is O(N) space
        # O(1) space requires 2 passes iirc.

        n = len(arr)

        i = k - 1

        arr[i].val, arr[~i].val = arr[~i].val, arr[i].val

        return head


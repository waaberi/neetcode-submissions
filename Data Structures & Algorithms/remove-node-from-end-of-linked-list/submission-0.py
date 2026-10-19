# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        """
        If you wanna do it in one pass, it requires extra space
        otherwise, you'll have to do it in 2 passes
        """

        arr = []
        ptr = head
        while ptr:
            arr.append(ptr)
            ptr = ptr.next
        
        length = len(arr)

        if length == n:
            return head.next

        arr.append(None) # just in case
        before = arr[length - n - 1]
        after = arr[length - n + 1]
        before.next = after

        return head

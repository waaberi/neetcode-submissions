# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        lst = []
        ptr = head
        while ptr:
            lst.append(ptr)
            ptr = ptr.next
        
        n = len(lst)

        prev = ListNode()

        """
        n = 4


        []
        """

        for i in range(n // 2 + n % 2):
            left = i
            right = n - i - 1
            prev.next = lst[left]
            lst[left].next = lst[right]
            prev = lst[right]
        
    

        prev.next = None
        

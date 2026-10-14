# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from math import gcd

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head

        while ptr.next is not None:
            cur = ptr
            next = ptr.next
            new = ListNode(gcd(cur.val, next.val))
            cur.next = new
            new.next = next
            ptr = next

        return head
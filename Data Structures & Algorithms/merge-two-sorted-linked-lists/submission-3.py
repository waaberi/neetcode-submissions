# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # I was previously doing it in place lol, lemme do it with a new one
        sol = ListNode()
        ptr = sol
        while list1 != None and list2 != None:
            if list1.val > list2.val:
                ptr.next = ListNode(list2.val)
                list2 = list2.next
            else:
                ptr.next = ListNode(list1.val)
                list1 = list1.next
            ptr = ptr.next
        
        if list1 == None:
            ptr.next = list2
        elif list2 == None:
            ptr.next = list1
            
        return sol.next
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def print_lst(lst: ListNode):
    while lst != None:
        print(lst.val, end=" ")
        lst = lst.next
    print()

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        .
        1 -> 2 -> 4
        1 -> 3 -> 5

             .
        1 -> 2 -> 4
             1 -> 3 -> 5

                  .
        1 -> 1 -> 3 -> 5
                  2 -> 4

                       .
        1 -> 1 -> 2 -> 4
                       3 -> 5

                            .
        1 -> 1 -> 2 -> 3 -> 5
                            4

                            .
        1 -> 1 -> 2 -> 3 -> 4
                            5

        """

        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val > list2.val:
            list1, list2 = list2, list1 # swap to ensure that i return list1

        root = list1

        p1 = None

        while list1 != None:
            # print_lst(root)
            # print_lst(list1)
            # print_lst(list2)
            # print()
            if list1.val > list2.val:
                p1.next = list2
                list2 = list1
                list1 = p1.next

            p1 = list1
            list1 = list1.next

        p1.next = list2


        return root
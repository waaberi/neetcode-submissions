class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr1 = m - 1
        ptr2 = n - 1
        store_in = m + n - 1
        while ptr1 >= 0 and ptr2 >= 0:
            if nums2[ptr2] > nums1[ptr1]:
                nums1[store_in] = nums2[ptr2]
                ptr2 -= 1
            else:
                nums1[store_in] = nums1[ptr1]
                ptr1 -= 1
            store_in -= 1
        while ptr1 >= 0:
            nums1[store_in] = nums1[ptr1]
            ptr1 -= 1
            store_in -= 1
        while ptr2 >= 0:
            nums1[store_in] = nums2[ptr2]
            ptr2 -= 1
            store_in -= 1
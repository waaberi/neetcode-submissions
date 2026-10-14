/*

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

*/

class Solution {
    /**
     * @param {number[]} nums1
     * @param {number} m
     * @param {number[]} nums2
     * @param {number} n
     * @return {void} Do not return anything, modify nums1 in-place instead.
     */
    merge(nums1: number[], m: number, nums2: number[], n: number): void {
        let ptr1 = m - 1;
        let ptr2 = n - 1;
        let store_in = m + n - 1;
        while (ptr1 >= 0 && ptr2 >= 0) {
            if (nums2[ptr2] > nums1[ptr1]) {
                nums1[store_in] = nums2[ptr2];
                ptr2--;
            } else {
                nums1[store_in] = nums1[ptr1];
                ptr1--;
            }
            store_in--;
        }

        while (ptr2 >= 0) {
            nums1[store_in] = nums2[ptr2];
            ptr2--;
            store_in--;
        }
    }
}

def merge(nums1, m, nums2, n):
    """************************
        given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

    Merge nums1 and nums2 into a single array sorted in non-decreasing order.

    The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


        Args:
            nums1 (list): list of int
            m (int): expexcted lenth of elements from nums1 list
            nums2 (list): list of int
            n (int): expexcted lenth of elements from 2 list
    """
    nums1[m:] = nums2[:n]
    nums1.sort()


nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [5, 6, 7]
merge(nums1, 3, nums2, 3)
print(nums1)

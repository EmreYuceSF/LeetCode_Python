def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    total_len = len(nums1)+len(nums2)
    
    
    nums3 = []
    
    while nums1 and nums2:
        if nums1[-1]>= nums2[-1]:
            nums3.append(nums1.pop())
        else:
            nums3.append(nums2.pop())
    left_over = nums1+nums2
    nums3 = nums3 + left_over[::-1]

    if  total_len%2:
        return nums3[int((total_len-1)/2)]
    else: 
        return (nums3[int(total_len/2)]+nums3[int(total_len/2 - 1)])/2
    
a=findMedianSortedArrays([1,2],[3,4])
print(a)
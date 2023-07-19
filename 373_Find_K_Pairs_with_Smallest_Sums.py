def kSmallestPairs(nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
    import heapq
    res = []
    for num1 in nums1:
        for num2 in nums2:
            heapq.heappush(res, [num1, num2])
    return res[:k]
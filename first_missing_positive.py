def firstMissingPositive(nums: list[int]) -> int:
    import heapq
    mint = 0
    for i in range(len(nums)):
        if nums[i] <= 0:
            nums[i] = float("inf")
    heapq.heapify(nums)
    for i in range(1, len(nums)):
        mint = heapq.heappop(nums)
        if i != mint:
            return i
    return mint+1
a= firstMissingPositive([1])
print(a)

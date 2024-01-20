def minSubArrayLen(target: int, nums: list[int]) -> int:
    if target in nums:
        return 1
    
    total = sum(nums)
    ln = len(nums)
    if  total < target:
        return 0
    if  total == 0:
        return ln
    j = 0
    total = 0
    subarray = 10**5
    from functools import cache
    @cache
    def find_subarray(i, j):
        nonlocal subarray, total
        total += nums[i]
        while total >= target:
            subarray = min((i -j+1), subarray)
            total -= nums[j]
            j+=1
        return subarray
        
    
    for i in range(ln):
        find_subarray(i,j)
    
    if subarray != float("inf"):
        return subarray
    else:
        return 0
    
print(minSubArrayLen(7, [2,3,1,2,4,3]))
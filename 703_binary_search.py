def search(nums: list[int], target: int) -> int:
    """ if target in nums:
        return nums.index(target)
    return -1 """
    
    
    ln = len(nums)
    start = 0
    end = ln - 1
    def find_mid():
        nonlocal start, end
        return (end+start)//2
        
    while start<=end:
        mid = find_mid()
        if target<nums[mid]:
            end = mid-1
        elif target> nums[mid]:
            start = mid +1 
        else:
            return mid
    return -1


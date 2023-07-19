def minSubArrayLen(target: int, nums: list[int]) -> int:
    nums.sort()
    ln  = len(nums)
    if nums[0] >= target:
        return 1
    if nums[-1] < target:
        total = 0
        for i in range(len(nums)):
            if total < target:
                total += nums[-1-i]
            else:
                return i + 1
        if total >= target:
            return ln
        else:
            return 0
    else:
        return 1
            
print(minSubArrayLen(213,[12,28,83,4,25,26,25,2,25,25,25,12]))
          
            
    
    
        
    
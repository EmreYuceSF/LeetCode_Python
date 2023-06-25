def longestSquareStreak(nums: list[int]) -> int:
    nums = set(nums)
    res_len = -1
    for num in nums:
        for i in range(2, 7):
            num *= num
            if num not in nums:
                break
            res_len = max(res_len, i)
        
    print (res_len)
            
            
        
    

longestSquareStreak([4,3,6,16,8,2])   
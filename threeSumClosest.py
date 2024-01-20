def threeSumClosest(nums: list[int], target: int) -> int:
    
    nums.sort()
    three_total = sum(nums[:3])
    diff = abs(target - three_total)
    length = len(nums)
   
    
    for i in range(length-2):
            sec_num_i = i+1
            thr_num_i = length-1 
            while sec_num_i < thr_num_i:
                if (total:= (nums[i] + nums[sec_num_i] + nums[thr_num_i])) == target:
                    return target
                elif total < target:
                    sec_num_i += 1
                elif total > target:
                    thr_num_i -= 1

                if abs(total - target) > diff:
                    pass
                else:
                    diff = abs(target - total)
                    three_total = total
    return three_total
                
    
    
    
    
nums = [1,1,1,5,5,5,5,5,5]
tar = 14

print(threeSumClosest(nums, tar))

        
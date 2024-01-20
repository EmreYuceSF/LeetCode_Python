def fourSum(nums: list[int], target: int) -> list[list[int]]:
    res = []
    ln = len(nums)
    for n1 in range(ln):
        for n2 in range(n1+1,ln):
            for n3 in range(n2+1,ln):
                a = nums[n1]
                b = nums[n2]
                c = nums[n3]
                d = target - a - b - c
                if d in nums[n3:] and sorted([a,b,c,d]) not in res:
                    res.append(sorted([a,b,c,d]))
    return res
         
    
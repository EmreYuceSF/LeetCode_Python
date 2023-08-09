def singleNumber(nums: list[int]) -> int:
    total = sum(nums)
    set_num = set(nums)
    return abs(total - int(sum(set_num)*2))


a= singleNumber([1])
print(a)

def divide(dividend: int, divisor: int) -> int:
    if dividend ==0:
        return 0
    res = 0
    res_mod = 1
    if (dividend < 0 and divisor > 0) or (dividend >0 and divisor<0):
        res_mod = -1
    divisor = abs(divisor)
    dividend = abs(dividend) 
        
    while True:
        if dividend <  divisor:
            break
        dividend -= divisor
        res += 1
        
    
    if res_mod == -1:
        return 0 - res
    return res



print(divide(1,-1))
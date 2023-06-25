def fib(n: int) -> int:
    if n == 0:
        return 0 
    temp = 1
    total = 1
    while n > 2:
        total += temp
        temp = total - temp
        n -= 1
    return total  

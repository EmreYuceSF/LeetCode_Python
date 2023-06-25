def tribonacci(n: int) -> int:
    '''function finds the n-th elements by creating a list 
    and list's n-th elements value is comes from sum of last 3 elements before n-th
    elemets.
    
    Arg: n int
    return: int
    '''

    my_list = [0,1,1,2]
    if n < 4:
        return my_list[n]
    else:
        for i in range(4, n+1):
            my_list.append(2*(my_list[i-1])-(my_list[i-4]))
        """ for i in range(n-2):
            my_list.append((my_list[-1]+my_list[-2]+my_list[-3])) """
    return my_list[n]
        
        
   
""" [0,1,1,2,4,7,13,24,44,81,149...]
    [, , ,0,0,-1,-1,-2,-4,-7,-13...]

l[n] = 2*(l[n-1]) - (l[n-4]) """
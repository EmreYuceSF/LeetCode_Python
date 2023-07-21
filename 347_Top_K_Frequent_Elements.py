def topKFrequent(nums: list[int], k: int) -> list[int]:
    mydict = {}
    res = []

    for num in nums:
        if num not in mydict:
            mydict[num] = 1
        else:
            mydict[num]+=1
    mydict = dict(sorted(mydict.items(), key=lambda item:item[1], reverse=True))
    
    for key in mydict.keys():
        res.append(key)
    return res[:k]

        
        
        
        
         
print(topKFrequent([3,0,1,0],1))
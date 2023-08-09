def topKFrequent(words: list[str], k: int) -> list[str]:
    from collections import Counter
    """  res = []
        my_dict = {}
        for word in words:
            if word not in my_dict:
                my_dict[word] = 1
            else:
                my_dict[word]+=1
                
        
        my_dict_sorted=(sorted(my_dict.items(), key = lambda x: (-x[1], x[0]))
        
        
        for i in range(k):
            res.append(my_dict_sorted[i][0])
        return res """
    
    count = Counter(words)
    
    return sorted(count.keys(), key = lambda x:(-count[x], [x]))[:k]
    
    
        
        
   


        
print(topKFrequent(["i","love","leetcode","i","love","coding"],3))
    
    
    
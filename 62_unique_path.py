
def unique_path(m, n):
    row = [1]*n
    for i in range(m-1):
        for j in range(n-2,-1,-1):
            row[j] = row[j]+row[j+1] 
    return row

        
        
                    
    

        
            
            
        
            
    
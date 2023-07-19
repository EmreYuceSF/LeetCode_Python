a = [0]
def creat_spots(n):
    for i in range(n):
        a.append([])

def store_in_a(x):
    if len(a) == 1:
       m = input("How many list dou youn wanty in your list: ")
       n = int(m)
       a[0] = n
       creat_spots(n)
    i  = x%a[0]  
    a[i+1].append(x)
  
ans = 'y'  
while ans == 'y':
    x= int(input("enter the num you want to store in the array"))
    
    store_in_a(x) 
    print(a)
    ans = (input("wanna in put more? (y/n)")).lower()


        
    
    
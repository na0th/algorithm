def solution(n, k):
    import math
    i = 0
    arr = [_+1 for _ in range(n)]
    
    n = n-1
    
    new_list =[]
    for i in range(n):
        mok = math.factorial(len(arr)-1)
        print(arr)
        
        a = k // mok
        b = k % mok
        
        if a != 0 and b == 0 :
            a-=1
            b=mok
            print("!!")
        k = b
        
        c=arr.pop(a)
        print(a,b,c)
        print(arr)
        print()
       
        
                    
        new_list.append(c)
    new_list.append(arr[0])
    print(new_list)
    return new_list
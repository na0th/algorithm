def solution(clothes):
    from collections import defaultdict
    dic = defaultdict(int)       
    
    for clothes_set in clothes:
        dic[clothes_set[1]] += 1
        
    
    list1 = []
    
    for key,value in dic.items() :
        list1.append(value)
        
    res = 1    
    for num in list1:
       res = res*(num+1) 
    
    
    
    answer=res-1
    return answer
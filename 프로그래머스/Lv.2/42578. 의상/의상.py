def solution(clothes):
#   (얼굴 종류+1)*(상의 종류+1)*(하의 종류+1)*(겉옷 종류+1) -1 (다 안 입으면 안됨)
#  종류 + 1 의 이유는 아무것도 착용 안한 경우 1개 추가..
    from collections import defaultdict
    
    
    dic = defaultdict(int)
    
    
    for item in clothes :
        dic[item[1]] += 1
        # if item[1] not in dic :
        #     dic[item[1]] = 1
        # else :
        #     dic[item[1]] += 1
        
    result = 1
    print(dic)
    for k,v in dic.items() :
        result = result * (v+1)
    result-=1
    return result
    
   
                      
    
    
    
    
    
    
    
    
    
#     from collections import defaultdict
#     dic = defaultdict(int)       
    
#     for clothes_set in clothes:
#         dic[clothes_set[1]] += 1
        
    
#     list1 = []
    
#     for key,value in dic.items() :
#         list1.append(value)
        
#     res = 1    
#     for num in list1:
#        res = res*(num+1) 
    
    
    
#     answer=res-1
#     return answer
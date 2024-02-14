def solution(topping):
#   크기 상관없이 토핑의 종류의 개수가 더 중요하다

# 슬라이싱으로 2개로 나눈 다음에 dic Counter 쓰면 되지 않을까?
    from collections import Counter 
    
    cnt = 0
    list1 = []
    list2 = topping
    
    dic1={}
    dic2=Counter(list2)
    

    for i in range(len(topping)-1):
        # print(dic1,dic2)
        if topping[i] not in dic1:
            dic1[topping[i]] = 1
        else :
            dic1[topping[i]] += 1
        
        if dic2[topping[i]] -1 == 0 :
            del dic2[topping[i]]
        else :
            dic2[topping[i]]-=1
        
        if len(dic1.keys()) == len(dic2.keys()) :
            cnt+=1
    answer = cnt
    return answer
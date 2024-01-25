def solution(k, tangerine):
#    수확 귤중 k개를 골라 판매
#     서로다른 종류를 최소화..
# counter해서 앞에서 부터 더해서 넘기면 되지 않을까..?
    
    from collections import Counter
    dic = dict(Counter(tangerine))
    
#   key로 정렬  
    # dic = dict(sorted(dic.items()))
    # print(dic)
    
#   value로 정렬
    # dic = dict(sorted(dic.items(),key=lambda x:x[1],reverse=True))
    
    value_list = list(dic.values())
    value_list.sort(reverse=True)
    # print(value_list)
    
    total = 0
    cnt = 0
    for value in value_list:
        if total >= k :
            break
        else :
            total += value
            cnt += 1
            
    return cnt
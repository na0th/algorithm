def solution(orders, course):
#     orders가 20이하 = 사람이 20명이 최대
#     인당 주문 최대 10개
#     2 3 4 5 6 7 8 9 10 
#     10c2 10c3 10c4 10c5 

#     그냥 완전탐색 가능할 것 같다..  
    from itertools import combinations
    dic = dict()
    for order in orders :
        order_list = list(order)
#       왜 정렬 안해서 주냐고
        order_list.sort()
        for i in range(2,len(order_list)+1):
            combo = list(combinations(order_list,i))
            for combi in combo :
                combi = ''.join(combi)
                if combi not in dic :
                    dic [ combi ] = 1
                else : 
                    dic [ combi ] +=1
                    
    dic = dict(sorted(dic.items(),key=lambda x:(x[1]),reverse=True))
    
    dic2 = dict ()
    for k,v in dic.items():
        if v == 1 :
            dic[k] = 0
        else :
            if len(k) not in dic2 :
                dic2[ len(k) ] = v
#            ex {2:3}
            else :
                if v < dic2 [ len(k) ]  :
                    dic[ k ] = 0
                if v > dic2 [ len(k) ] :
                    dic2[ len(k) ] = v
                    
    
    print(dic)
    print(dic2)
    
    answer = []
    for k,v in dic.items():
        if v != 0 :
            if len(k) in course :
                answer.append(k)    

    answer.sort()
            
    
    
        
    
    return answer
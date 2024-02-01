def solution(want, number, discount):
#   1가지 제품을 하루에 1개만 구매가능
#   정현이는 원하는 제품과 수량이 할인하는 날짜와 10일연속 일치시 회원가입
    
#   셋째 날부터..
    start = 0 
    end = 9
    
    cnt = 0
    for i in range(len(discount)):
        start = i
        end = start + 10
        
        if len(discount)-i < 10 :
            end = len(discount)
            
        
        dic = dict()
        for idx,item in enumerate(want):
            dic[item] = number[idx]
#       딕셔너리에 banana:3, apple:2 등록
        for j in range(start,end) :
            if discount[j] in dic :
                dic[discount[j]]-=1
                
        # print(dic)
        
        check = -1        
        for k,v in dic.items() :
            if v >= 1 :
                check = 0
        if check == -1 :
            cnt+=1
                
            
  
    answer = cnt
    return answer
def solution(weights):
    weights.sort()

#   전부 카운팅하기
#   2개 이상인 애들을 추리고 nC2해서 서로 간에 곱하는 것을 더하고
#   똑같은 애들끼리 경우의 수를 더한다. ex) 100 100 100 100이면 경우의수 6개
#   ex 100 100 100 200 200 200이면 100끼리 3개 200끼리 3개 100,200 9개..

    from collections import Counter 
    
    dic = dict(Counter(weights))
    # dic = sorted(dic,key=lambda x:x)
    # print(dic)
    add_list = list(dic.items())

    cnt = 0
    for i in range(len(add_list)) :
        for j in range(i+1,len(add_list)) :
            if add_list[i][0]*4 == add_list[j][0]*3 :
                cnt += add_list[i][1]*add_list[j][1]
            elif add_list[i][0]*3 == add_list[j][0]*2 :
                cnt += add_list[i][1]*add_list[j][1]
            elif add_list[i][0]*2 == add_list[j][0] :
                cnt += add_list[i][1]*add_list[j][1]
    for i in range(len(add_list)):
        if add_list[i][1] > 1 :
            cnt += add_list[i][1]*(add_list[i][1]-1)*(1/2)

    return cnt
    
        
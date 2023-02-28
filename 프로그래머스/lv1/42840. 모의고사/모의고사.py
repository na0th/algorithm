def solution(answers):
#   정답 순서를 리스트로 만든다
    one_way = [1,2,3,4,5]
    two_way = [2,1,2,3,2,4,2,5]
    three_way = [3,3,1,1,2,2,4,4,5,5]
#  정답 카운트 변수    
    cnt_1 = 0
    cnt_2 = 0
    cnt_3 = 0
#   정답 리스트 원소 수에 맞게 %5 , %8 , %10 한다
    for i in range(len(answers)):
        i_1 = i % 5
        i_2 = i % 8
        i_3 = i % 10
        if one_way[i_1] == answers[i] :
            cnt_1+=1
        if two_way[i_2] == answers[i] :
            cnt_2+=1
        if three_way[i_3] == answers[i] :
            cnt_3+=1
            
    answer = []
    
    dic={}
    dic[1] = cnt_1
    dic[2] = cnt_2
    dic[3] = cnt_3
    
    max(dic,key=dic.get)

# print([k for k,v in dic.items() if max(dic.values()) == v])
#   value값이 최대인 key를 찾아서 리스트에 ..
    answer = [k for k,v in dic.items() if max(dic.values()) == v]
    return answer
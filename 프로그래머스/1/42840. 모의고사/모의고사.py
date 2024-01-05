def solution(answers):
    
# answers의 원소 개수까지의 1번 정답 리스트, 2번 정답 리스트, 3번 정답 리스트를 만들어야 한다..

# ex) 1은 1,2,3,4,5,1,2,3,4,5 쭉쭉
    list1 = [1,2,3,4,5]
    list2 = [2,1,2,3,2,4,2,5]
    list3 = [3,3,1,1,2,2,4,4,5,5]

    answer1=[]
    answer2=[]
    answer3=[]
    for i in range(len(answers)):
        answer1.append(list1[i%len(list1)])
        answer2.append(list2[i%len(list2)])
        answer3.append(list3[i%len(list3)])
            
    cnt1=0
    cnt2=0
    cnt3=0
    
    for i in range(len(answers)):
        if answers[i] == answer1[i]:
            cnt1+=1
        if answers[i] == answer2[i]:
            cnt2+=1
        if answers[i] == answer3[i]:
            cnt3+=1  
            
#   5,0,0이 나yhj오는 건 알겠는데 여기서 어떻게 return을 높은 점수 사람대로..?      
    dic= {}
    dic[1]=cnt1
    dic[2]=cnt2
    dic[3]=cnt3
    dic = sorted(dic.items(), key= lambda item:item[1],reverse=True)
    
    answer = []
    
    print(dic)
    
    for i in range(len(dic)):
        if answer :
            if dic[0][1] == dic[i][1] :
                answer.append(dic[i][0])
        if not answer :
            answer.append(dic[0][0])
        
    answer.sort()

    return answer
        
    


    
    
# #   정답 순서를 리스트로 만든다
#     one_way = [1,2,3,4,5]
#     two_way = [2,1,2,3,2,4,2,5]
#     three_way = [3,3,1,1,2,2,4,4,5,5]
# #  정답 카운트 변수    
#     cnt_1 = 0
#     cnt_2 = 0
#     cnt_3 = 0
# #   정답 리스트 원소 수에 맞게 %5 , %8 , %10 한다
#     for i in range(len(answers)):
#         i_1 = i % 5
#         i_2 = i % 8
#         i_3 = i % 10
#         if one_way[i_1] == answers[i] :
#             cnt_1+=1
#         if two_way[i_2] == answers[i] :
#             cnt_2+=1
#         if three_way[i_3] == answers[i] :
#             cnt_3+=1
            
#     answer = []
    
#     dic={}
#     dic[1] = cnt_1
#     dic[2] = cnt_2
#     dic[3] = cnt_3
    
#     max(dic,key=dic.get)

# # print([k for k,v in dic.items() if max(dic.values()) == v])
# #   value값이 최대인 key를 찾아서 리스트에 ..
#     answer = [k for k,v in dic.items() if max(dic.values()) == v]
#     return answer
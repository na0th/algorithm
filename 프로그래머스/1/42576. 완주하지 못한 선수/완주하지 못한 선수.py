def solution(participant, completion):
#  1명빼고 전부 마라톤 완주했음
#  배열로 참가자 배열/ 완주자 배열이 주어짐 
#  10^6이니까 시간복잡도가 n^2을 넘기면 안되겠다.   

 
# participant의 배열을 하나 씩 completion에 있는지 없는지 in을 이용해 해볼까? 없다면 그것 출력
    
    # for member in participant :
    #     if member in completion :
    #         continue;
    #     answer = member
    # return answer
# 해보니 시간초과.. participant가 n개고, completion이 n-1개니까..
# 리스트에서 in 키워드로 연산하면 n의 연산을 2번 하는 거니 O(n^2)임..

# 여기서 아.. in 연산을 딕셔너리에서 하면 시간복잡도를 확 줄이겠군..

# 딕셔너리에 completion을 추가하고, participant를 돌면서 in 키워드로 딕셔너리에 participant의 원소가 있는지 확인하고 없으면 return 끝.
    from collections import Counter
    count_dict = Counter(participant)
    
    
    for i in range(len(completion)):
        if completion[i] in count_dict :
            count_dict[completion[i]]-=1
    
    for k,v in count_dict.items():
        if v == 1 :
            return k
        
        
    # for key,value in count_dict.items() :
    #     print(key,value)
        
        
   
    
        
 # 기존 풀이법
#     dic1={}
#     for i in range(len(participant)):
#         if participant[i] not in dic1 :
#             dic1[participant[i]] = 1
#         else : 
#             dic1[participant[i]] +=1
    
#     dic2={}
#     for i in range(len(completion)):
#         if completion[i] not in dic2 :
#             dic2[completion[i]] = 1
#         else : 
#             dic2[completion[i]] +=1
   
#     for i in range(len(completion)):
#         if completion[i] in dic1 :
#             dic1[completion[i]] -=1
        
#     answer=""
#     for k,v in dic1.items():
#         if v == 1:
#             answer=k
#             return answer
   
#     return answer
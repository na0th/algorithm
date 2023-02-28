def solution(participant, completion):
#     1명빼고 전부 마라톤 완주했음
#  배열로 참가자 배열/ 완주자 배열이 주어짐 
#  10^6이니까 시간복잡도가 n^2을 넘기면 안되겠다.   

    dic1={}
    for i in range(len(participant)):
        if participant[i] not in dic1 :
            dic1[participant[i]] = 1
        else : 
            dic1[participant[i]] +=1
    
    dic2={}
    for i in range(len(completion)):
        if completion[i] not in dic2 :
            dic2[completion[i]] = 1
        else : 
            dic2[completion[i]] +=1
   
    for i in range(len(completion)):
        if completion[i] in dic1 :
            dic1[completion[i]] -=1
        
    answer=""
    for k,v in dic1.items():
        if v == 1:
            answer=k
            return answer
   
    return answer
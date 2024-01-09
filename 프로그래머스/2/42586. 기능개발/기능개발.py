def solution(progresses, speeds):
    
#    speeds에서 맨 앞을 뽑는다..
#    temp라는 변수에 저장해서 계속 더하다 100을 넘기면 계속 뽑는다..
# #    cnt 변수로 count해서 추가한다..
    
    answer = []
    i = 0
    while(i < len(progresses)) :
#       계속 + 시켜서 100을 넘기게 만드려고..
        for j in range(i,len(progresses)):
            progresses[j] += speeds[j]
#       내가 100을 넘겼을 때,    
        if progresses[i] >= 100 :
            cnt = 0
            for k in range(i,len(progresses)):
#               100보다 작은 게 나오면 for문 종료(배포 count 중단)
                if progresses[k] < 100 :
                    break
                else : 
                    cnt+=1
                    
            if i < len(progresses):    
                i = i+cnt  
                    
            answer.append(cnt)
            continue

    return answer


    
    
    
    
    
    
    
    
#     answer = []
#     day_list=[]
#     for i in range(len(progresses)) :
#         for j in range(100):
#             if progresses[i]+j*speeds[i] >= 100 :
#                 day_list.append(j)
#                 break
#     i=1
#     count=1
#     num = day_list[0]
#     while(i<len(day_list)):
#         if num >= day_list[i] :
#             count+=1
#         else :
#             answer.append(count)
#             num = day_list[i]
#             count=1
#         if i == len(day_list)-1 :
#             answer.append(count)
#         i+=1
            
            
            
        
        
    
    
#     print(day_list)    
#     return answer
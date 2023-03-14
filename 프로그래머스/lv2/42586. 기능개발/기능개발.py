def solution(progresses, speeds):
    
    answer = []
    day_list=[]
    for i in range(len(progresses)) :
        for j in range(100):
            if progresses[i]+j*speeds[i] >= 100 :
                day_list.append(j)
                break
    i=1
    count=1
    num = day_list[0]
    while(i<len(day_list)):
        if num >= day_list[i] :
            count+=1
        else :
            answer.append(count)
            num = day_list[i]
            count=1
        if i == len(day_list)-1 :
            answer.append(count)
        i+=1
            
            
            
        
        
    
    
    print(day_list)    
    return answer
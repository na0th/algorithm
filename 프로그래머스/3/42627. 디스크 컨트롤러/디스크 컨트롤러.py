def solution(jobs):
#   작업 요청을 끝마쳤을 때, 그때 가능한 처리 작업중 가장 소요시간이 적은 것 순으로..
#  맨처음엔 처음부터 가능한 것만 가능할 것..
    time = 0
    i = 0
    min_worktime = 1001
    idx = 0
    
    len_jobs = len(jobs)
    sum = 0 
    while(jobs):
        if jobs[i][0] <= time :
            if min_worktime >=jobs[i][1] :
                min_worktime = jobs[i][1]
                idx = i
        if i == len(jobs)-1 :
            if min_worktime == 1001 :
                i = 0
                time+=1
                continue
            time+=min_worktime
            sum+=(time-jobs[idx][0])
            del jobs[idx]
            i = 0
            idx = 0
            min_worktime = 1001
            continue
        i+=1
    return int(sum/len_jobs)
    
            
                
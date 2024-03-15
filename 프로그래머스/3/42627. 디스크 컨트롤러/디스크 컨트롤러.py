def solution(jobs):
#   작업 요청을 끝마쳤을 때, 그때 가능한 처리 작업중 가장 소요시간이 적은 것 순으로..
#  맨처음엔 처음부터 가능한 것만 가능할 것..
    time = 0
    i = 0
#   문제 조건에서 시간 소요가 1000까지임을 확인함
    min_worktime = 1001
    idx = 0
#   jobs가 줄어들기때문에 len(jobs)가 변할 것이라 미리 저장해둠
    len_jobs = len(jobs)
    sum = 0 
    while(jobs):
        if jobs[i][0] <= time :
            if min_worktime >=jobs[i][1] :
                min_worktime = jobs[i][1]
                idx = i
        if i == len(jobs)-1 :
#           min_worktime이 인덱스 전부를 돌았는데도 1001이라는 건 아무것도 그 시간에 어떤 작업도 할 수 없다는 뜻이므로 시간을 +1초 시키기
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
#         int 함수로 소수점 제거
    return int(sum/len_jobs)
    
            
                
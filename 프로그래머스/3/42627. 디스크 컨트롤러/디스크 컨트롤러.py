def solution(jobs):
    import heapq
    from collections import deque
    '''
    jobs 힙으로 만들어서 최소 시간 작업요청만 계속 뽑기
    
    1)작업 요청 시간순, 소요 시간 순으로 정렬
    
    지금 시간에 할 수 있는 작업들을 리스트에 시간만 추가  ex [남은 작업시간 ]
    작업이 추가될 때 시간만 heappush
    
    if 지금 할 수 있는 작업 없다
    있다 -> heappop해서 time에서 더하기
    
    break 언제 ? 
    heappop만 한 건 카운트해서 len(jobs)가 되면 끝
    
    
    다 끝나면 끝난 시간만 계산
    '''
    jobs.sort(key=lambda x:(x[0],x[1]))
    boolean_job = [False for _ in range(len(jobs))]
    print(jobs)
    heap = []
    time = 0
    cnt = 0
    start_sum = 0
    for job in jobs :
        start_sum += job[0]
    end_sum = 0
    while(cnt<len(jobs)) :
        # print(time)
        if heap :
            short_job = heapq.heappop(heap)
            time+=short_job
            end_sum+=time
            cnt+=1
        for i,job in enumerate(jobs) :
            if time < job[0]:
                if not heap :
                    time+=1
                break
            elif time >= job[0] and boolean_job[i] == False:
                heapq.heappush(heap,job[1])
                boolean_job[i] = True
            
                
                
        
        
    
    
    return (end_sum-start_sum)//len(jobs)
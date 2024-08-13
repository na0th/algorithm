def solution(targets):
    import heapq
    
    '''
    heapify 시키고, heappop을 해. (start,end)꼴인데 
    while문으로 if end > heap[0][0]이면 pop해,
    end가 더 작거나 같으면 break하고 cnt+1시켜
    '''
    
    answer = 0

    heap = []
    for target in targets:
        heapq.heappush(heap, (target[0],target[1]))
        
    # print(heap)

    while heap:
        start, end = heapq.heappop(heap)
        answer += 1
        min_end = end
        while heap:
            next_start, next_end = heap[0]
            min_end = min(min_end, next_end)
            if next_start < min_end :
                heapq.heappop(heap)
            else:
                break

    return answer

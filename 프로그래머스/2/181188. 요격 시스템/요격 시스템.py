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
        heapq.heappush(heap, (target[1],target[0]))
        
    while heap:
        end,start = heapq.heappop(heap)
        answer += 1
        min_heap = end
        while heap:
            next_end, next_start = heap[0]
            if next_start < min_heap :
                heapq.heappop(heap)
            else:
                break

    return answer

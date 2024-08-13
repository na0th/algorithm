def solution(targets):
    import heapq
    from collections import deque
    # targets.sort(key=lambda x:x[1])
    # print(targets)
    '''
    heapify 시키고, heappop을 해. (start,end)꼴인데 
    while문으로 if end > heap[0][0]이면 pop해,
    end가 더 작거나 같으면 break하고 cnt+1시켜
    '''
#     heap = []
#     for f,s in targets :
#         f , s = s , f
#         heapq.heappush(heap,(f,s))

#     # heapq.heapify(targets)
#     print(heap)
    
    '''
    정렬 후 스택
    '''
    
    targets.sort(key = lambda x:x[1])
    # print(targets)
    
    stack = deque(targets)
    cnt = 0
    while(stack) :
        start, end = stack.popleft()
        
        while(stack and stack[0][0] < end) :
            stack.popleft()
        cnt += 1
    return cnt
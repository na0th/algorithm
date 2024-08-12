def solution(n, k, enemy):
    import heapq
    '''
    n명으로 막기
    k번의 라운드 넘기기
    막다가 막을 수 없으면 지나간 라운드에서 최대값을 뽑아서 부활시킨다
    
    
    '''
    heap = []

    for i,v in enumerate(enemy):
        if n >= v :
            n -= v
            heapq.heappush(heap,-v)
        elif k > 0 :
#           최대값을 확인하고 뽑는 것..
            if heap and v <= -1*heap[0] :
                n += (-1*heapq.heappop(heap)-v)
                heapq.heappush(heap,-v)
#           힙의 최대값보다 크면 어떻게 할 수가 없으니 방어막만 쓴다
            k-=1
        else : 
            return i
    return i+1



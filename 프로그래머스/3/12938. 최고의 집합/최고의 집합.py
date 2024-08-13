def solution(n, s):
    import heapq
    '''
    1.각 원소의 합이 S가 되는 수의 집합
    2. 위 조건을 만족하면서 각 원소의 곱이 최대
    
    if n<s : return -1
    
    else :
    
    차례대로 +1씩 해주는 게 best 같은데?    
    '''
    if n > s : 
        return [-1]
    elif n == s :
        return [1 for i in range(n)]
    else :
        q = s // n
        mod = s % n
        
        heap = [q for i in range(n)]
        heapq.heapify(heap)
        while(mod > 0):
            if heap:
                min_heap = heapq.heappop(heap)
                min_heap+=1
                heapq.heappush(heap,min_heap)
            mod-=1
        
        heap.sort()
        return heap
    
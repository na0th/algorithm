def solution(storey):
    import heapq
    from collections import deque

    '''
        마법의 정수 층으로 이동하는데  현재 위치 + 버튼 값 < 0  --> 이동하지 않는다.
        storey에서 0층까지 최소한으로 가기..
        
        BFS로 (2554,0) -> (2550,4) , (2560,5) 이렇게 나눠짐.. (255,4), (256,5)로..
        또 저거에 대해서 또 해..
        그러다 힙..? << 생각이 필요해보임.
        최소 횟수를 뽑았을 때, 0이 나온다? 그게  최소값
    '''
    dic = {0:0,1:1,2:2,3:3,4:4,5:5,6:5,7:4,8:3,9:2}
    result = []
    def bfs(start_node, graph):
        queue = deque([(start_node,0)])

        while queue:
            curr_num, cnt = queue.popleft()
            if 0<= curr_num < 10 :
                result.append(cnt + dic[curr_num])
                continue 
            
            q = curr_num // 10
            m = curr_num % 10 
            
            queue.append((q,cnt+m))
            queue.append((q+1,cnt+10-m))

        # print(result)   
        return min(result)
   
    return bfs(storey,0)
    
    
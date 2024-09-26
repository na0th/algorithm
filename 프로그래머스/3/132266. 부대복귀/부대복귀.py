def solution(n, roads, sources, destination):
    from collections import defaultdict
    import heapq
    '''
    최단 시간으로 복귀
    road [1,2] = 1과 2는 연결되어 있고, 걸리는 시간은 1이다.
    '''
    graph = defaultdict(list)

    for item in roads :
        graph[item[0]].append((item[1],1))
        graph[item[1]].append((item[0],1))
        
    # print(dict(graph))
    # graph = dict(graph)
    
    def dijkstra(graph,start) :
        costs = {}
        pq = []
        heapq.heappush(pq, (0, start))
        
        while pq :
            cur_cost, cur_v = heapq.heappop(pq)
            if cur_v not in costs:
                costs[cur_v] = cur_cost
                
                for next_v,cost in graph[cur_v] :
                    next_cost = cur_cost + cost
                    heapq.heappush(pq, (next_cost, next_v))
        
        return costs
    
    answer = []
    costs = dijkstra(graph, destination)
    for source in sources:
        if source in costs:
            answer.append(costs[source])
        else:
            answer.append(-1)
    return answer
    

    
                    
        
            
    
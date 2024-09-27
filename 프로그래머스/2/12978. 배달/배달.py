def solution(N, road, K):
    from collections import defaultdict
    import heapq
    answer = 0
    dic = defaultdict(list)
    for item in road :
        dic[item[0]].append((item[1],item[2]))
        dic[item[1]].append((item[0],item[2]))

    # print(dic)
    # print()
    def dijkstra(graph, start):
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
        # print(costs)
    
    costs = dijkstra(dic,1)
    cnt = 0
    for k,v in costs.items():
        if v<=K :
            cnt+=1
    return cnt
    # print(costs)

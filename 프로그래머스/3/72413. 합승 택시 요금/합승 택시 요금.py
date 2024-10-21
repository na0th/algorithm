def solution(n, s, a, b, fares):
    from collections import defaultdict
    import heapq
    '''
    문제 내용 :
    무지는 택시 이용시 어피치가 비슷한 방향으로 가는 걸 확인
    택시 합승을 적절히 이용해서 택시요금을 아낄 수 있나    
    s에서 같이 타서. 합승을 적절히 이용해서.. a,b 둘 다 귀가할 때 귀가 그때의 최소 비용
    각자 이동하는 경우의 택시요금이 더 낮다면? 합승을 하지 않아도 됨 따로 따로 합이 작을 때..
    
    알고리즘 분류 :
    그래프, 플로이드 와샬? 
    
    어떻게 풀이? 
    플로이드 와샬을 통해 s에서 모든 정점까지의 거리를 구함
    무한대가 아닌 값들을 다 뒤지면서 + 모든 정점에서 집까지 a,b 거리를 구해서 더함 
    그중 최소를 찾으면 되지 않을까?
    
    
    s에서 특정 지점까지 다익스트라 다 구해..
    a에서 특정 지점까지 다익스트라 다 구해..
    b에서 특정 지점까지 다익스트라 다 구해서.. 특정 지점에서 d를 전부 더해
    
    그중 최소 찾으면 특정지점에서 s에서 특정지점까지가서 , a가는비용,b가는비용 다 더해진 것
    
    
    1) 그래프 꼴로 만들기
    2) s,a,b에서 특정지점까지 최소 거리를 다익스트라로 다 구함
    3) 그냥 다 더해서 최소값 찾기
    '''
    graph = defaultdict(list)
    for fare in fares :
        graph[fare[0]].append([fare[1],fare[2]])
        graph[fare[1]].append([fare[0],fare[2]])
    # print(graph)
    
    def dijkstra(graph, start):
        costs={}
        pq =[]
        heapq.heappush(pq,(0,start))
        
        while pq:
            cur_cost, cur_v= heapq.heappop(pq)
            if cur_v not in costs:
                costs[cur_v] = cur_cost
                for next_v, cost in graph[cur_v]:
                    next_cost = cur_cost + cost
                    heapq.heappush(pq,(next_cost,next_v))
                    
        return costs
    
    
    temp = dijkstra(graph,s)
    
    for k,v in dijkstra(graph,a).items() :
        if k in temp :
            temp[k]+=v
    for k,v in dijkstra(graph,b).items() :
        if k in temp :
            temp[k]+=v

    return min(temp.values())



    
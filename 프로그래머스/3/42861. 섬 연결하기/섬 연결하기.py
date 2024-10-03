def solution(n, costs):
    from collections import defaultdict
    from itertools import combinations
    import heapq
    '''
    n개의 섬 사이에 다리를 건설하는 비용이 주어질 때
    리턴 : 모든 섬이 통행 가능하도록 만드는 최소의 비용
    
    플로이드 와샬? BFS?
    다익스트라 여러 번
    그래프에서 주어진 특정 지점에서 다른 특정지점까지의 최단 거리중 제일 큰 값 리턴
    
    
    '''
    #그래프 만들기
#     graph = defaultdict(list)
#     for cost in costs:
#         # cost[0]에서 cost[1]까지의 거리는 cost[2]
#         graph[cost[0]].append([cost[1],cost[2]])
#         # cost[1]에서 cost[0]까지의 거리는 cost[2]
#         graph[cost[1]].append([cost[0],cost[2]])
        
#     print(graph)
    
    # 비용이 낮은 순으로 정렬
    costs.sort(key=lambda x:x[2])
    # print(costs)
    total_cost = 0
    # 부모 테이블 초기화
    parent = [0]*(n+1)
    for i in range(1,n+1):
        parent[i] = i
        
    # print(parent)
    #부모가 같은지 찾자
    def find_parent(parent,x):
        if parent[x] != x :
            parent[x] = find_parent(parent,parent[x])
        #나랑 내 부모가 같다면 걔는 부모임
        return parent[x]
    #a,b 비교하는데 find 연산으로 부모가 다르다면? 사이클 형성 x니까 트리에 포함
    def union_parent(parant,a,b):
        a = find_parent(parent,a)
        b = find_parent(parent,b)
        
        #
        if a < b :
            parent[b] = a
        else :
            parent[a] = b
            
            
    for item in costs:
        a,b,cost = item[0],item[1],item[2]
        if find_parent(parent,a) != find_parent(parent,b) :
            union_parent(parent,a,b)
            total_cost+=cost
            
    return total_cost

    
    
    

    
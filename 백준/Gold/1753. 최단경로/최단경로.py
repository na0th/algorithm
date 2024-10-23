from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
# print(v,e)
start_point = int(input())
# print(start_point)

graph = defaultdict(list)
for _ in range(e):
    start,end,distance = map(int,input().split())
    graph[start].append([distance,end])
    # graph[end].append([start,distance])

# print(graph)

# a -> b 로 가는 간선이 여러 개 있다.

def dijkstra(graph,start):
    costs={}
    pq = []
    heapq.heappush(pq,(0,start))

    while pq :
        cur_cost, cur_v = heapq.heappop(pq)
        if cur_v not in costs :
            costs[cur_v] = cur_cost
            for cost, next_v in graph[cur_v]:
                next_cost = cur_cost + cost
                heapq.heappush(pq,(next_cost,next_v))
    return costs

costs = dijkstra(graph,start_point)
# print(costs)

for i in range(1,v+1):
    if i == start_point:
        print(0)
    elif i not in costs :
        print("INF")
    else :
        print(costs[i])


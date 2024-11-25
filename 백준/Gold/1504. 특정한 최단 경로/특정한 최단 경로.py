'''
1번에서 N번 정점으로 최단 거리 이동

임의로 주어진 두 정점은 반드시 통과
최단 경로 이동


알고리즘 분류 : 최단거리-> 다익스트라 or 플루이드와샬

어떻게 풀이 ? :
1번에서 n번으로 이동하는데 맨 마지막 u,v를 거쳐서 가는 최단거리..

1) 1-> u - > v -> n
2) 1-> v -> u -> n  둘을 비교..

1-> v 까지 다익스트라
v -> u 까지 다익스트라
v-> n 까지 다익스트라

그냥 시작이 1인 다익스트라, 시작이 v인 다익스트라 , 시작이 n인 다익스트라 구하기..

'''
import sys
from collections import defaultdict
import heapq
n,e = map(int,sys.stdin.readline().split())

# print(n,e)

graph = defaultdict(list)

for _ in range(e):
    start,end,dist = list(map(int,sys.stdin.readline().split()))
    graph[start].append([dist,end])
    graph[end].append([dist,start])
# print(graph)

u,v = map(int, sys.stdin.readline().split())

def dijkstra(start,end):
    costs = {}
    pq = []
    heapq.heappush(pq,(0, start))

    while pq :
        cur_cost, cur_v = heapq.heappop(pq)
        if cur_v not in costs :
            costs[cur_v] = cur_cost
            for cost, next_v in graph[cur_v]:
                next_cost = cost + cur_cost
                heapq.heappush(pq,(next_cost,next_v))
    return costs.get(end, float('inf'))


path1 = dijkstra(1, v) + dijkstra(v, u) + dijkstra(u, n)
path2 = dijkstra(1, u) + dijkstra(u, v) + dijkstra(v, n)

result = min(path1, path2)
print(-1 if result == float('inf') else result)

'''
1-> u + 공통 -> v ->n
1-> v +공통 -> u->n
1-> u -> v -> n
1-> v -> u -> n
'''
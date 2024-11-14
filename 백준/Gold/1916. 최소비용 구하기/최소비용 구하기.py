import sys
from collections import defaultdict
import heapq
'''
문제 내용 : N개 정점. M개의 간선 a -> b 까지 최소 비용
첫째 줄에 정점 N, 둘째 줄에는 간선 M
1 2 2 => 1에서 2까지 비용 2
출발점에서 도착점을 갈 수 있는 경우만 입력으로 주어짐

단방향.. 버스니까!

알고리즘 분류 : 가중치 비용이 주어졌을 때, 최소 비용
-> A에서 B까지 최소 비용
-> 다익스트라

어떻게 풀이 ?
1 2 2 -> 1(start) : [2(distance),2(end)]
'''

n = int(sys.stdin.readline())
m  = int(sys.stdin.readline())

graph = defaultdict(list)
for _ in range(m):
    start, end , dist = map(int, sys.stdin.readline().split())
    graph[start].append([dist,end])

start, end = map(int,sys.stdin.readline().split())

def dijkstra(graph,start):
    costs = {}
    pq = []
    heapq.heappush(pq,(0,start))

    while pq:
        cur_cost, cur_v = heapq.heappop(pq)
        if cur_v not in costs :
            costs[cur_v] = cur_cost
            for cost, next_v in graph[cur_v]:
                next_cost = cur_cost + cost
                heapq.heappush(pq,(next_cost,next_v))
    return costs


costs = dijkstra(graph,start)
# print(dijkstra(graph,start))
print(costs[end])
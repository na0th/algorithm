# x에서의 다익스트라 쓰면 되지 않을까?

import sys
from collections import defaultdict
import heapq
n,m,x = map(int,sys.stdin.readline().split())

# print(n,m,x)
graph = defaultdict(list)
for _ in range(m):
    start,end,dist = map(int,sys.stdin.readline().split())
    graph[start].append([dist,end])

def dijkstra_from_x(graph,start):
    costs = {}
    pq = []
    heapq.heappush(pq, (0,start))
    while pq :
        cur_cost, cur_v = heapq.heappop(pq)
        if cur_v not in costs:
            costs[cur_v] = cur_cost
            for cost, next_v in graph[cur_v] :
                next_cost = cur_cost + cost
                heapq.heappush(pq,(next_cost,next_v))
    return costs
def dijkstra_to_x(graph,start,final):
    costs = {}
    pq = []
    heapq.heappush(pq, (0,start))
    while pq :
        cur_cost, cur_v = heapq.heappop(pq)
        if cur_v not in costs:
            costs[cur_v] = cur_cost
            for cost, next_v in graph[cur_v] :
                next_cost = cur_cost + cost
                heapq.heappush(pq,(next_cost,next_v))
    return costs[final]

temp_list1 = []
for go in range(1,n+1):
    temp_list1.append(dijkstra_to_x(graph,go,x))
temp_list2 = sorted(dijkstra_from_x(graph,x).items(),key=lambda x:x[0])
temp_list2 = [x[1] for x in temp_list2]
# print(temp_list2)
result = [x+y for x,y in zip(temp_list1,temp_list2)]
# print(temp_list1)
# print(temp_list2)
# print(result)
print(max(result))


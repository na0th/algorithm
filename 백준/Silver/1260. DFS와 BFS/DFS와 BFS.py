'''

첫 째줄
n 정점 갯수
m 간선 개수
v 탐색 시작할 정점 번호

간선은 양방향, 두 정점 사이 여러 개의 간선이 존재
방문할 수 있는 정점이 많다면, 정점 번호가 작은 것을 먼저 방문
더 이상 방문할 수 있는 점이 없는 경우 종료


알고리즘 분류 : BFS, DFS (문제 제목에 나와있음)

어떻게 풀이 ?

DFS 스택, 재귀
BFS 큐
'''
import sys
from collections import defaultdict
n,m,v = map(int, sys.stdin.readline().split())

# print(n,m,v)

graph = defaultdict(list)
for _ in range(m):
    start, end = map(int,sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

for key in graph:
    graph[key].sort()
# print(graph)

def dfs(visited,start_point):
    visited.append(start_point)
    print(start_point,end=" ")
    for next_v in graph[start_point]:
        if next_v not in visited:
            dfs(visited,next_v)

dfs(visited=[], start_point=v)
print()
def bfs(visited,start_point):
    queue = ([start_point])
    visited.append(start_point)
    while queue:
        current = queue.pop(0)
        for next_v in graph[current]:
            if next_v not in visited:
                visited.append(next_v)
                queue.append(next_v)
    print(*visited)

bfs(visited=[],start_point=v)

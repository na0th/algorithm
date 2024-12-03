'''
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다.
 (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N(N-1)/2)
 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다.
 (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다

알고리즘 분류 :
같은 요소 모으기 DFS?, Union-Find ?

어떻게 풀이?
Graph 형태로 만든다
DFS 형태로 끝까지 뒤져서 SET으로 묶고 CNT+1?

1: 2,5
2: 1,5
3: 4
4: 3,6
5: 1,2
'''
import sys
sys.setrecursionlimit(10**6)
from collections import defaultdict
n,m = map(int,sys.stdin.readline().split())

graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(visited,start):
    if start not in visited:
        visited.append(start)
        for next_v in graph[start]:
            if next_v not in visited:
                dfs(visited,next_v)

visited = []
cnt = 0

for node in range(1,n+1):
    if node not in visited:
        dfs(visited,node)
        cnt += 1
print(cnt)
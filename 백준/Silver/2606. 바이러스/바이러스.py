'''
네트워크 상 바이러스가 걸리면, 연결된 전체 네트워크가 웜 바이러스에 걸린다
1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번을 통해 웜 바이러스에 걸리는 컴퓨터 수 출력

알고리즘 분류 : DFS, Union Find?

어떻게 풀이?
graph 형식으로 바꿔서 dfs를 한다 visited에 없으면 넣고 +1 ...
쭉 해서 count를 리턴

'''

import sys
from collections import defaultdict
u = int(sys.stdin.readline())
v = int(sys.stdin.readline())

graph = defaultdict(list)
for _ in range(v) :
    start, end = map(int,sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

# print(graph)

def dfs(visited,start):
    #base case
    if start in visited :
        return 0
    visited.add(start)

    count = 1
    for next_v in graph[start]:
        count += dfs(visited, next_v)

    return count

visited = set()
group_count = dfs(visited,1)
print(group_count-1)
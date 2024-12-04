'''
모든 지점에 대해서 목표지점까지의 거리를 구하기
가로와 세로로만 움직일 수 있다

n은 세로의 크기, m은 가로의 크기다
0은 갈 수 없는 땅이고
1은 갈 수 있는 땅,
2는 목표지점이다.

입력에서 2는 단 한개이다.

알고리즘 분류 : 모든 목표지점까지의 거리? BFS로 QUEUE에 계속 넣어주면 될 것 같다.

어떻게 풀이?
start 뽑고 -> 가로,세로 queue에 담고
-> 조건따져서 가능한지 판별(방문했는지,방문 가능한지)
-> depth+1 해서 전부를  queue에서  꺼내면 끝
'''


import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())

graph = [list(map(int, input().split())) for _ in range(n)]


def find_start(graph):
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2 :

                return (i,j)

def bfs(start, graph):
    result_graph = [[-1] * m for _ in range(n)]

    queue = deque([(start[0],start[1],0)])
    visited = set()
    visited.add((start[0], start[1]))
    result_graph[start[0]][start[1]] = 0
    start = find_start(graph)



    directions  = [(0,1),(0,-1),(-1,0),(1,0)]


    while queue:
        x,y,depth = queue.popleft()

        for dx,dy in directions :
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 0 and (nx,ny) not in visited:
                visited.add((nx,ny))
                result_graph[nx][ny] = depth + 1
                queue.append((nx,ny,depth+1))
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                result_graph[i][j] = 0
    return result_graph
start = find_start(graph)
result_graph= bfs(start,graph)

for i in range(n):
    for j in range(m):
        print(result_graph[i][j],end=" ")
    print()

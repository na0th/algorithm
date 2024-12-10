'''
1은 이동 가능 0은 이동 불가능
(1, 1)에서 출발하여 (N, M)의 이동 최소 칸 수 구하기
인접한 칸으로만 이동 가능
칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.


알고리즘 분류 : 전형적인 BFS 같음
어떻게 풀이 ?
count를 queue에 추가 (x,y,count) 형식


'''

import sys
from collections import deque
n,m = map(int, sys.stdin.readline().split())

graph = [list(map(int, line.strip())) for line in sys.stdin.read().splitlines()]

# print(graph)
def bfs():
    visited = set()
    queue = deque()
    queue.append((0,0,1))

    while queue:
        x,y,count = queue.popleft()
        if x == n-1  and y == m-1 :
            return count
        dxdy = [(1,0),(0,1),(-1,0),(0,-1)]
        for dx,dy in dxdy :
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0<= ny < m and graph[nx][ny] == 1 and (nx,ny) not in visited:
                visited.add((nx,ny))
                queue.append((nx,ny,count+1))
print(bfs())



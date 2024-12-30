'''
상하좌우 이동 가능

o : 빈 공간
x : 벽
i : 도연이
p : 사람

출력 : 도연이가 만날 수 있는 사람의 수 출력
아무도 만나지 못하면 'TT'를 출력

알고리즘 분류 : 백트래킹?

어떻게 풀이 ?
백트래킹으로 갈 수 있는 곳을 다 가본다.
사람을 만나면 이동해서 O로 바꿈.

'''

import sys
sys.setrecursionlimit(10**6)
n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    row = list(sys.stdin.readline().strip())
    graph.append(row)


def dfs(x,y):
    #base case(갈 수 있는 곳이 없으면 return)
    #상하좌우
    global cnt
    dxdy = [(1,0),(0,1),(-1,0),(0,-1)]

    for dx,dy in dxdy:
        nx, ny = x+dx, y+dy
        if 0<= nx < n and 0<= ny < m and graph[nx][ny] != 'X':
            if (nx,ny) not in visited :
                visited.add((nx,ny))
                if graph[nx][ny] == 'P' :
                    cnt+=1
                dfs(nx,ny)



cnt = 0
visited = set()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'I':
            dfs(i,j)



if cnt == 0:
    print("TT")
else :
    print(cnt)
import sys
sys.setrecursionlimit(10000)
def solution(maps):
    from collections import deque

    def dfs(start_x, start_y, graph,cnt):
        
        if maps[start_x][start_y] == 'X' :
            return
        cnt += int(maps[start_x][start_y])
        visited.add((start_x,start_y))

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for i in range(4):
            nx = (start_x) + dx[i]
            ny = (start_y) + dy[i]

            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                if (nx, ny) not in visited and maps[nx][ny] != 'X':
                    visited.add((nx, ny)) 
                    cnt = dfs(nx,ny,maps,cnt)
                          
        return cnt
    
    visited = set()
    result = []
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if (i, j) not in visited and maps[i][j] != 'X':
                result.append(dfs(i,j,maps,0))
    if not result :
        return [-1]
    else :
        return sorted(result)

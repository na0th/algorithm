
def solution(maps):
    from collections import deque

    def bfs(x,y):
        cnt = 0
        queue = deque()
        
        queue.append((x,y))    
        visited.add((x,y))
        
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]

        while(queue):
            x, y = queue.popleft()
            cnt+=int(maps[x][y])
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < len(maps) and 0<= ny < len(maps[0]) :
                    if (nx,ny) not in visited and maps[nx][ny] != 'X' :
                        queue.append((nx,ny))
                        visited.add((nx,ny))
                        
        return cnt
    result = []
    visited = set()
    for i in range(len(maps)):
        for j in range(len(maps[0])) :
            if maps[i][j] != 'X' and (i,j) not in visited :
                result.append(bfs(i,j))
    return sorted(result) if result else [-1]
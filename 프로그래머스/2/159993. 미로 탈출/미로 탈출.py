def solution(maps):
    '''
    최소값이니까 일단 BFS 세팅
    레버까지 최소로 가기 + 레버에서 출구까지 최소로 가기
    다른 것은 여러 번 지나갈 수 있다?.. 레버에 도착하면 visited를 초기화 하면 되겠다
    '''
    from collections import deque

    def bfs_first(start_x, start_y, graph):

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        queue = deque([(start_x, start_y,0)])
        visited = set([(start_x, start_y)])
        
        while queue:
            
            x, y, cnt= queue.popleft()
            if graph[x][y] == 'L' :
                return cnt

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                    if (nx, ny) not in visited and maps[nx][ny] != 'X' :
                        visited.add((nx, ny))
                        queue.append((nx, ny,cnt+1))
        return -1
    
    def bfs_second(start_x, start_y, graph):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        queue = deque([(start_x, start_y,0)])
        visited = set([(start_x, start_y)])
        
        while queue:
            
            x, y, cnt= queue.popleft()
            if graph[x][y] == 'E' :
                return cnt
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                    if (nx, ny) not in visited and maps[nx][ny] != 'X' :
                        visited.add((nx, ny))
                        queue.append((nx, ny,cnt+1))
        return -1
    
    start_x, start_y = 0, 0
    lever_x, lever_y = 0, 0
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                start_x, start_y = i, j
            elif maps[i][j] == 'L':
                lever_x, lever_y = i, j
                
    if bfs_first(start_x,start_y,maps) != -1 and bfs_second(lever_x,lever_y,maps) != -1 :
        return bfs_first(start_x,start_y,maps)+bfs_second(lever_x,lever_y,maps)
    else :
        return -1

    
    
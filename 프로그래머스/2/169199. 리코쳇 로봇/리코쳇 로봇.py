def solution(board):
    '''
    최소 움직임? BFS로 간다
    어떻게 -1을 리턴하지?
    
    '''
    from collections import deque

    def bfs(start_x, start_y, graph):

        queue = deque([(start_x, start_y,0)])
        visited = set([(start_x, start_y)])

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        while queue:
            x, y, cnt = queue.popleft()

#           어떻게 상하좌우 일직선 방향 쭉 체크를 하지?
#          상/ 하 / 좌 / 우 체크해서 D를 만나면 1칸전에서 멈춰 그게 G면 탈출
            
            for i in range(4) :
                nx = x
                ny = y 
                while 0 <= nx+dx[i] < len(graph) and 0 <= ny+dy[i] < len(graph[0]):
                    
                    if board[nx+dx[i]][ny+dy[i]] == 'D' :
   
                        break
                    nx += dx[i]
                    ny += dy[i]
                if board[nx][ny] == 'G' :
                    return cnt+1
                
                if (nx,ny) not in visited:
                    visited.add((nx,ny))
                    queue.append((nx,ny,cnt+1))
                
                
#                 while 0 <= nx+dx[i] < len(graph) and 0 <= ny+dy[i] < len(graph[0]) and board[nx + dx[i]][ny + dy[i]] != 'D':
#                     nx += dx[i]
#                     ny += dy[i]
#                 if board[nx][ny] == 'G' :
#                         return cnt+1    

#                 if (nx,ny) not in visited:
#                     visited.add((nx,ny))
#                     queue.append((nx,ny,cnt+1))

                    
                    
                    
                    

        return -1
    startX, startY = 0, 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R' :
                startX = i
                startY = j
                
    return bfs(startX,startY,board)
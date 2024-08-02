from collections import deque
def solution(maps):
#     최단거리는 BFS라 했는데..
#     BFS는 Queue, Linked List로 구현한다 했었고
    
    start = (0,0)
    def BFS(maps,start):
        rows, cols = len(maps), len(maps[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        queue = deque([start])
        visited = set()
        visited.add(start)
        
        
        while(queue):
            current = queue.popleft()
            x, y = current
            
            if x == rows-1 and y == cols-1:
                # print(distance)
                return maps[x][y]
                
            for direction in directions:
                nx, ny = x + direction[0], y + direction[1]
                if 0 <= nx < rows and 0 <= ny < cols:
                    if maps[nx][ny] == 1 and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
                        maps[nx][ny] = maps[x][y] + 1
        return -1
    
    visited_positions = BFS(maps, start)
    return visited_positions

def solution(n, edge):
    from collections import defaultdict
    from collections import deque
    '''
    bfs 구현?
    '''
    dic = defaultdict(list)
    for v in edge :
        dic[v[0]].append(v[1])
        dic[v[1]].append(v[0])
        
    # print(dic)
    
    def bfs(start_node, graph):
        a_list = [1]
        queue = deque([(start_node,1)])
        visited = set([start_node])
        
        while queue:
            curr_node, cnt = queue.popleft()

            for next_node in graph[curr_node]:
                if next_node not in visited:
                    visited.add(next_node)
                    queue.append((next_node,cnt+1))
                    if max(a_list) <= cnt+1 :
                        a_list.append(cnt+1)
            max_value = max(a_list)
            
        return a_list.count(max_value)
            
    
    return bfs(1,dic)

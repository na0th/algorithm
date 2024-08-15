
def solution(n, computers):
    '''
    [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    이 형태를
    {
    1: 2
    2: 3 
    } 형태로 바꿔야 하나?
    
    일단은 해보기로
    '''
    
    graph = {}
    for idx, item in enumerate(computers) :
        if idx+1 not in graph :
            graph[idx+1] = []
        for index, check in enumerate(item) :
            if check == 1 and index != idx:
                graph[idx+1].append(index+1)
    print(graph)
    
    visited = set()
    cnt = 0
    def dfs(curr_node,graph,visited) :
        nonlocal cnt
        visited.add(curr_node)
        for next_node in graph[curr_node]:
            if next_node not in visited :
                dfs(next_node,graph,visited)
                
    
    for k in graph :
        if k not in visited :
            dfs(k,graph,visited)
            cnt+=1
        
                
    return cnt
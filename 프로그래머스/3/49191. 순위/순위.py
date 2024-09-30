def solution(n, results):
    from collections import defaultdict
    '''
    1 ... N번 
    권투는 1:1이고, 실력이 좋다면 항상 이깁니다.
    
    순위를 매기려는데, 몇몇 경기 결과는 없다..
    리턴 : 정확하게 순위를 매길 수 있는 선수의 수
    [A,B]는 A가 B를 이겼다는 뜻이다.
    
    부모 노드와 자식노드의 합이 N-1이면 순위를 매길 수 있음.
    나를 이기는 사람의 합 + 나한테 지는 사람의 합
    
    1: 2
    2: 5
    3: 2
    4 : 2, 3
    5 : X 
    이렇게 주어졌을 떄, 도달 가능한지 딕셔너리 형태로 나타낼 수 있나?
    '''
    reachable1 = defaultdict(set)
    reachable2 = defaultdict(set)
    
    dic1 = defaultdict(list)
    dic_back = defaultdict(list)
    for item in results :
        dic1[item[0]].append(item[1])
    for item in results :
        dic_back[item[1]].append(item[0])
    print(dic1) 
    print(dic_back)
    
    def dfs(node, visited,dic):
        if node not in dic:
            return
        for neighbor in dic[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                dfs(neighbor, visited,dic)
                
    for start_node in dic1.keys():
        visited = set()
        dfs(start_node, visited,dic1)
        reachable1[start_node] = list(visited)
        
    for start_node in dic_back.keys():
        visited = set()
        dfs(start_node,visited,dic_back)
        reachable2[start_node] = list(visited)
    print(reachable1)
    print(reachable2)
    cnt = 0
    all_keys = set(reachable1.keys()) | set(reachable2.keys())
    for key in all_keys : 
        total = 0 
        if key in reachable1.keys() :
            total += len(reachable1[key])
        if key in reachable2.keys() :
            total += len(reachable2[key])
        
        if total+1 == n :
            cnt+=1
    return cnt
    
    
    # print(reachable1+reachable2)
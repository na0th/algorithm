def solution(n, wires):
    
#   답이 생각나지 않으니 제일 기본적으로 그냥 딕셔너리 만든 후 DFS 기본 꼴로 시도해보자
    def dfs(graph,start,visited=[]):
        
        visited.append(start)
        
        for node in graph[start]:
            if node not in visited :
                dfs(graph,node,visited)
                
        return visited
        
        
    from collections import defaultdict
    count_list = []
    for i in range(len(wires)):
        new_list = wires[:i]+wires[i+1:] 

        dict = defaultdict(list)
        for j in range(len(new_list)):
            dict[new_list[j][0]].append(new_list[j][1])
            dict[new_list[j][1]].append(new_list[j][0])
            
        print(new_list)    
        print(dict)
#       dict의 첫 번째 원소를 어떻게 가리키지..?
        keys = sorted(dict.keys())
        first_visit = keys[0]
        
        print(len((dfs(dict,first_visit,visited=[]))))
        # print(len(dfs(dict,first_visit,visited=[])))
        
        num_graph = len(dfs(dict,first_visit,visited=[]))
        count_list.append(abs(n-2*(num_graph)))
    print("결과",count_list)
        
        # print((dfs(dict,first_visit,visited=[])))
    
        

       

    return min(count_list)
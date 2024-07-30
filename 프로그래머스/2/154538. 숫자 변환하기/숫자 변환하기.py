from collections import deque
def solution(x, y, n):
    '''
    x를 y로 변환하기
    방식은 3가지
    1. x = x + n 
    2. x = x * 2
    3. x = x * 3
    
    리턴 : x를 y로 변환시키는 최소 연산 횟수
    x를 y로 만들 수 없다면 -1 
    
    최소 연산 횟수면...
    dfs? bfs? 탐색 같은데
    
    dfs는 재귀
    bfs는 큐
    
    최적의 답이니까 bfs
    최소 연산 횟수는 어떻게 구하지..
    어떻게 중단시키지..

    y를 넘으면 그만둬
    '''
#    
#         heap???

#     def bfs(x,y,n):
#        ex 3    // 4 6 9
#         queue = deque([x+n,2*x,3*x])
#         visited = set([x+n,2*x,3*x])

#     while queue:
#         curr_node = queue.popleft()
        
#         if min(queue) > y :
#             return -1
#         queue.extend([curr_node+n,curr_node*2,curr_node*3])
        
#         for next_node in visited:
#             if next_node not in visited:
#                 visited.add(next_node)
#                 queue.append(next_node)
    
    def bfs(x, y, n):
        q = deque()
        cnt[x] = 1
        q.append(x)
        
        
        
        while q :
            num = q.popleft()
           
            if 0 <= num+n and num+n <=  1000000 and cnt[num+n] == 0:
                cnt[num+n] = cnt[num] + 1
                q.append(num+n)
            if 0<= 2*num and 2*num <=  1000000 and cnt[2*num] == 0:
                cnt[num*2] = cnt[num] + 1
                q.append(num*2)
            if 0 <= 3*num and 3*num <=  1000000 and cnt[3*num] == 0: 
                cnt[num*3] = cnt[num] + 1
                q.append(num*3)
        
            
    cnt = [0] * 1000001   
    bfs(x,y,n)
    return cnt[y]-1


    

       
    
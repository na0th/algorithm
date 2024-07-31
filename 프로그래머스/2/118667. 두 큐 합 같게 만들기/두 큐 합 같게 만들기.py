def solution(queue1, queue2):
    '''
    길이가 같은 두 개의 큐에서 하나의 큐에서 빼서 다른 큐에 원소를 넣는다
    1번의 POP과 1번의 INSERT가 작업 1회
    큐이므로 먼저 집어넣은 원소를 빼는 것
    
    그래서 각 큐의 원소의 합을 같도록 하기
    리턴 : 최소 연산 횟수
    
    최적의 해니까 BFS 같다 
    
    1에서 먼저? 2에서 먼저 둘중에서 최소
    
    첫 번째에서 시작할 때 합이 절반보다 작으면 ? 2번째 
    
    while queue1 :
            if start_dif == 0 :
                # break
                return cnt
            if sum(queue1) < sum(queue2) :
                pick = queue2.popleft()
                queue1.append(pick)
                cnt+=1
            elif sum(queue1) > sum(queue2) :
                pick = queue1.popleft()
                queue2.append(pick)
                cnt+=1
                
        return -1
    '''
    from collections import deque
    queue1, queue2 = deque(queue1), deque(queue2)
    
    def bfs1(queue1, queue2) :
        cnt = 0
        if sum(queue1) < sum(queue2) :
            queue1 , queue2 = queue2, queue1
        start_dif = sum(queue1)-sum(queue2)
        
        while queue1 :
            if cnt > 4* len(queue1):
                return -1
            if start_dif == 0 :
                # break
                return cnt
            if  start_dif < 0 :
                pick = queue2.popleft()
                queue1.append(pick)
                start_dif += 2*pick
                cnt+=1
            elif start_dif > 0 :
                pick = queue1.popleft()
                queue2.append(pick)
                start_dif -= 2*pick
                cnt+=1
                
        return -1
    
    
    return bfs1(queue1,queue2)




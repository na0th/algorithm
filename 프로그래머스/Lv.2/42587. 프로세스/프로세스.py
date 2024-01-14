def solution(priorities, location):
    
    from collections import deque
    
    new_list =[[idx,prior] for idx,prior in enumerate(priorities)]
    deque1 = deque(new_list)
    
    cnt = 0
    print(deque1)
    
#     while(1):
#         if not deque1 :
#             break
#         pop_item = deque1.popleft()
#         if pop_item[1] == max(deque1, key=lambda x: x[1])[1]: 
#             cnt+=1
#             if pop_item[0] == location:
#                 return cnt
                
#         else :
#             deque1.append(pop_item)
        
       

        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# #   일단, location에 있는 값이랑 나중에 pop한 값을 비교하기 위해서
# #   값을 저장해놓을 리스트를 만들어야 할 것 같다.

#     work_list = [_ for _ in range(len(priorities))]
    
# #   나중에 리턴될 값을 기억해놓자, 그래야 비교해서 return을 줄 수 있다.
#     memo_num = work_list[location]

# #  priorities를 돌면서 나보다 우선순위 높은 작업이 있으면 
# #  dequeue 후 , enqueue 맨 앞에서 빼서 맨 뒤로 보낸다
# # __ ___계속 돌아야 하는데 어떻게 돌게 할까?_____ while(run)
# # len(priorities) > 1 and
#     count = 0
#     while(True):
#         if  priorities[0] < max(priorities[0:]):
#             priorities.append(priorities[0])
#             work_list.append(work_list[0])
#             del priorities[0]
#             del work_list[0]
#         else :
#             count+=1
#             if work_list[0] == memo_num :
#                 return count
#             del priorities[0]
#             del work_list[0]
            
# #  priorities를 돌면서 나보다 우선순위 높은 작업이 없으면 
# #  dequeue하고, 꺼낸 횟수 count+=1을 하고, memo_num과 비교한다.
# #  memo_num과 같으면 break 하고  count를 리턴해주면 도니다.
    
    
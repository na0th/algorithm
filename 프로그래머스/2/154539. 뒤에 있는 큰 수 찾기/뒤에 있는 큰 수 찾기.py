def solution(numbers):
    from collections import deque
#   n이 10^6.. nlogn 이하

#  슬라이싱 활용..? 
#     answer = []

#     for i in range(len(numbers)):
#         if i == len(numbers)-1 :
#             answer.append(-1)
#             break
#         if numbers[i] >= max(numbers[i+1:]) :
#             answer.append(-1)
#             continue
#         for j in range(i+1,len(numbers)):
#             if numbers[j] > numbers[i] :
#                 answer.append(numbers[j])
#                 break
#     return answer
        
#   위의 알고리즘 시간초과...
    
#   처음의 모두 result의 element를 0으로 초기화하고
#   스택을 정렬하면서 number와 스택 element들을 비교하는데, 
#   스택의 element가 number보다 작다면 계속 pop하고,number로 result에 리턴 끝나면 number를 push

# ex )) stack = [9,6,4]     number가 7이라면      4와 7 비교 4 pop, 6과 7비교 6 pop, 9와 7비교 = number가 작으니 그만//그리고 전부 number로 교체..(역으로) <- 이게 구현이 어려울 듯 싶다.. then, 7 push
#  stack = [9,7] (정렬된 상태)

# 연산이 모두 끝나고 0인 애들은 stack에서 pop 되지 않은 애들 = 큰 애를 못 난 애들 => 전부 -1로 바꾸기 


#  stack element가 number보다 작을 때, 작은 element들을 전부 number로 교체하는 과정을 하려면 인덱스가 필요하니까 enumerate를 써볼까?


    
    
    
#  number랑 똑같이 전부 0으로 만들기
#     result = [0 for _ in range(len(numbers))]
    
#     stack = []
    
    
#     enum_numbers = list(enumerate(numbers)) 
#     print(enum_numbers)
#     print()
    
#     while(enum_numbers) :
        
#         print(stack)
        
#         pick = enum_numbers.pop(0)
        
#         if not stack :
#             stack.append(pick)
#             continue
        
#         for item in stack:
#             # stack.pop(0)
#             if item[1] < pick[1] :
#                 result[item[0]] = pick[1]
#             elif item[1] == pick[1] :
#                 continue
#             else :
#                 print()
#                 break
  
# #           element가 stack보다 크거나 같으면 끝내고 푸쉬
   
# #       push
#         stack.append(pick)
    
#        # [1,2,4,5,8] 
#         stack.sort(key=lambda x:x[1]) 
    
#     for i in range(len(result)) :
#         if result[i] == 0 :
#             result[i] = -1
    
#     print(result)



            
   # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 
    # return result



    result = [0 for _ in range(len(numbers))]
    
    stack = deque()
    # stack = []
    len_numbers = len(numbers)
    enum_numbers = deque(enumerate(numbers)) 
    # enum_numbers = list(enumerate(numbers)) 
    
    stack.append((0,numbers[0]))
    del enum_numbers[0]
    
    for i in range(len_numbers-1):
        # pop_num = enum_numbers.pop(0)
        pop_num = enum_numbers.popleft()
        # print(pop_num)
        
        if pop_num[1] > stack[-1][1]:
            while(stack and stack[-1][1]<pop_num[1]):
                small_pop = stack.pop()
                # small_pop = stack.pop()
                result[small_pop[0]]=pop_num[1]
        
        stack.append(pop_num)
        
    for item in stack :
        result[item[0]]=-1
        
    return result
        
            
        

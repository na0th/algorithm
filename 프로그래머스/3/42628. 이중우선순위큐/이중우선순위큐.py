def solution(operations):
    stack_list = []
    for item in operations :
        if item == "D -1" :
            stack_list.sort()
            if stack_list :
                stack_list.pop(0)
        elif item == "D 1" :
            stack_list.sort()
            if stack_list :
                stack_list.pop(-1)
        else :
            temp =item.split(" ")
            temp[1]=int(temp[1])
            stack_list.append(temp[1])
    if stack_list :
        return [max(stack_list),min(stack_list)]
    else :
        return [0,0]
    # print(stack_list)
        
#     import heapq
#     min_heap = []
#     max_heap = []
    
#     heapq.heapify(min_heap)
#     heapq.heapify(max_heap)
    
#     for item in operations :
#         if item == "D -1" :
#             if len(min_heap) == 0 :
#                 continue
#             heapq.heappop(min_heap)
#         elif item == "D 1":
#             if len(max_heap) == 0 :
#                 continue
#             heapq.heappop(max_heap)
#         else :
#             temp =item.split(" ")
#             temp[1]=int(temp[1])
            
#             heapq.heappush(min_heap,temp[1])
#             heapq.heappush(max_heap,(-temp[1],temp[1]))

#     if min_heap :
       
#         num1 = heapq.heappop(max_heap)[1]
#         num2 = heapq.heappop(min_heap)
#         return [num1,num2]


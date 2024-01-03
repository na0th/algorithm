def solution(arr):
#   배열의 크기가 백만? 그럼 O(N)정도로 짜야할 듯..
#  answer 리스트에 추가하고, 같으면 continue하고 다르면 추가해서 리스트 1바퀴돌면 되지 않을까?


    answer = []
    answer.append(arr[0])
    k = 0
    for i in range(len(arr)):
        if answer[k] != arr[i]:
            k+=1
            answer.append(arr[i])
    return answer

#     for i in range(len(arr)):
#         if arr[i] not in   :
#             answer.append(arr[i])
#         else :
#             if i > 0 :
#                 if arr[i-1] != arr[i]:
#                     answer.append(arr[i])
#             continue
    
#     return answer
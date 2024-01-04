def solution(array, commands):
    answer = []

#누가봐도 정렬..
# 제한사항에서 전부 100 이하.. 시간복잡도는 자유롭다
# 슬라이싱해서, 정렬, k번째 인덱스 append 끝.

# 순회 O(N) * 정렬 O(NlogN)
    for i in range(len(commands)):
        new_list = []
        new_list = array[(commands[i][0]-1):commands[i][1]]
        new_list.sort()
        print(new_list)
        answer.append(new_list[(commands[i][2]-1)])
    
    return answer
    
# 기존 풀이    
#   commands의 element 수만큼 반복한다.
#  리스트를 commands[0][0], commands[0][1]로 슬라이싱하고 거기서 찾는다

#     for i in range(len(commands)):
#         arr = array[(commands[i][0]-1):commands[i][1]]
#         arr.sort()
#         print(arr)
#         answer.append(arr[(commands[i][2]-1)])
    
    
    
#     return answer
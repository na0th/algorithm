def solution(n, lost, reserve):
#   일단 왼쪽 먼저 주고, 오른쪽 주는 걸로 해보자..
#  기본 셋팅을 1로해놓고, lost를 일단 0으로 만들고 시작
    cnt_list = [1 for x in range(n)]
    
    for i in range(len(lost)):
        cnt_list[lost[i]-1] = 0
    
    # print(cnt_list)
    
#   lost, reserve 정렬 
    lost.sort()
    reserve.sort()
#  왼쪽에서 오른쪽으로 이동하니..    
#    왼쪽 체크, 나,  오른쪽 체크 순 but, 여벌 체육복인 사람이 도난당하면 빌려줄 수 없다..

    for i in range(len(reserve)):
#       나 체크하기
        if reserve[i] in lost :
            cnt_list[reserve[i]-1] = 1
            continue
#       맨 왼쪽이 있으면 무조건 주기
        if reserve[i] == 1 :
            if cnt_list[0] == 0 :
                cnt_list[0] = 1
                continue
            cnt_list[1] = 1
            continue
            
#       왼쪽 먼저 체크    
        if cnt_list[reserve[i]-2] == 0 :
            cnt_list[reserve[i]-2] = 1
            continue

            
# 오른쪽 체크 맨 오른쪽이면 인덱스 에러니까 예외걸기
        if reserve[i] == n :
            continue
                
#  오른쪽주기
        if cnt_list[reserve[i]] == 0 :
            cnt_list[reserve[i]] = 1
            continue
            
        # if cnt_list[reserve[i]] == 0:
        #     if reserve[i] != n :
        #         cnt_list[reserve[i]] = 1
#             else :
#                 if cnt_list[n-2] == 0:
#                     cnt_list[n-2] = 1
#                     continue
                    
                    
                    
#         if reserve[i] == n :
#             if cnt_list[n-2] == 0 :
#                 cnt_list[n-2] = 1
#                 continue
#             if reserve[i] in lost :
#                 cnt_list[n-1] = 1
#             continue
            
#         if cnt_list[reserve[i]] == 0 :
#             cnt_list[reserve[i]] = 1


    return sum(cnt_list)    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
#   일단 여벌이 있는 학생중 도난 당했는지 아닌지를 체크해야 함
#   먼저 도둑맞은 reserve 학생들은 둘 다 제거하고 시작
#     lost.sort()
#     reserve.sort()
#     for i in range(len(reserve)):
#         if reserve[i] in lost:
#             lost.remove(reserve[i])
#             reserve[i] = 100
#             continue

#     for i in range(len(reserve)) :
# #    왼쪽부터 준다, 준다음은 continue로 넘어가게
#         if reserve[i]-1 in lost :
#             lost.remove(reserve[i]-1)
#             reserve[i] = 100
#             continue
            
#         if reserve[i]+1 in lost :
#             lost.remove(reserve[i]+1)
#             reserve[i] = 100
#             continue
            
        
    
#     answer = n-len(lost)
#     return answer
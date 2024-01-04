def solution(sizes):
#  sizes의 길이가 10000이하.. n^2 까지는 괜찮을 듯하다..?
#  greedy하게 계속 요건을 만족하는 것으로 다음 것과 비교하면 되지않을까?
#  ex) 명함 1은 60,50 이고 2까지되면 70 50이어야 함. 
#  그러면 그냥 명함 1개고 70, 50 있는 걸로 퉁쳐도 되지 않나?
#  이렇게 2개씩만 비교하면 될 듯하다..

    
    now_a = sizes[0][0]
    now_b = sizes[0][1]
    
    for i in range(len(sizes)):
        # print(now_a,now_b,"now_a,now_b")
        
        a=max(now_a,sizes[i][0])*max(now_b,sizes[i][1])
        b=max(now_a,sizes[i][1])*max(now_b,sizes[i][0])
        # print(a,b)
        if a >= b :
            now_a = max(now_a,sizes[i][1])
            now_b = max(now_b,sizes[i][0])
    
        if b > a :
            now_a = max(now_a,sizes[i][0])
            now_b = max(now_b,sizes[i][1])
            
        answer=min(a,b)
    
            
    
    
    return answer
    
    
#   그냥 제일 간단하게는 가로 최대, 세로 최대면 되는데
#   이것보다는 그냥 큰 놈들은 앞쪽으로 다 몰아넣고
#   작은 놈들은 다 뒤쪽으로 몰아넣고 구해볼까?

#   DP로 바로 직전 값들만 기억해서 최대값을 갱신해볼까?
#     max_f = 0
#     max_s = 0
#     for i in range(len(sizes)):
#         now_max = max(sizes[i][0],sizes[i][1])
#         now_min = min(sizes[i][0],sizes[i][1])
#         if max_f < now_max :
#             max_f = now_max
#         if max_s < now_min :
#             max_s = now_min
    
#     answer = max_f * max_s
#     return answer
def solution(sizes):
#   그냥 제일 간단하게는 가로 최대, 세로 최대면 되는데
#   이것보다는 그냥 큰 놈들은 앞쪽으로 다 몰아넣고
#   작은 놈들은 다 뒤쪽으로 몰아넣고 구해볼까?

#   DP로 바로 직전 값들만 기억해서 최대값을 갱신해볼까?
    max_f = 0
    max_s = 0
    for i in range(len(sizes)):
        now_max = max(sizes[i][0],sizes[i][1])
        now_min = min(sizes[i][0],sizes[i][1])
        if max_f < now_max :
            max_f = now_max
        if max_s < now_min :
            max_s = now_min
    
    answer = max_f * max_s
    return answer
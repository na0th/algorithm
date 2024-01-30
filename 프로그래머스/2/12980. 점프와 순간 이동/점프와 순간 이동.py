def solution(n):
    ans = 0
#   k칸 점프 or 현재까지 온 거리 2배 순간이동
#   점프를 최소화하고 2배 순간이동을 많이 써라

    ans = bin(n)[2:]
    count = 0
    for i in range(len(ans)) :
        if ans[i] == '1' :
            count+=1
    
    return count
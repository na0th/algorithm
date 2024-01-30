def solution(n):

#   k칸 점프 or 현재까지 온 거리 2배 순간이동
#   점프를 최소화하고 2배 순간이동을 많이 써라 
    return bin(n)[2:].count('1')
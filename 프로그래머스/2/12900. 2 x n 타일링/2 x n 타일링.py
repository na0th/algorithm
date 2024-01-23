def solution(n):
#   감이 DP네..
#   N=1일 때, N=2이 일때에서 N이 3일 때 간다고 치면
#   N=1일 때는, N=3으로 가면 N=1인 경우의 수에서 가로 직사각형 2개를 위아래로 붙히는 게 끝
#   N=2일 때는, N=3으로가면 직사각형을 세로로 붙히는 경우의 수 1개 끝
#   따라서 F(3) = F(1)+F(2)
#  일반화하면 F(N) = F(N-2)+F(N-1)
# 딕셔너리로 구현

    dic = {1:1,2:2}
    
    for i in range(3,n+1) :
        if i not in dic :
            dic[i]= dic[i-1]+dic[i-2] % 1000000007
            
    answer = dic[n] % 1000000007
    
    return answer
def solution(m, n, puddles):
    '''
    무조건 DP
    
    물에 잠긴 지역은 어떻게 계산할 것인가?
    경우의수  = 왼쪽에서 오는 경우 + 위쪽에서 내려오는 경우
    예외처리 필요
    
    
    '''
    check = [[0 for i in range(m)] for j in range(n)]
    # print(check)
    check[0][0] = 1
    for i in range(n):
        for j in range(m) :
            if [j+1,i+1] in puddles :
                continue
            else: 
                if 1 <= i <= n : 
                    check[i][j]+=check[i-1][j]
                if 1<= j <= m: 
                    check[i][j]+=check[i][j-1]
    # print(check)
    return check[n-1][m-1] % 1000000007
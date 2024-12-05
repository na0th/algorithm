'''
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다.
합을 나타낼 때는 수를 1개 이상 사용해야 한다.

알고리즘 분류 : DP

어떻게 풀이 ?

F(N) = F(N-1)+F(N-2)+F(N-3)
왜냐면 F(N-1)+1 or F(N-2)+2 OR F(n-3)+3

'''

import sys
n = int(sys.stdin.readline())

dp = {1:1,2:2,3:4}
for _ in range(n):
    num = int(sys.stdin.readline())
    for i in range(4,num+1):
        if i not in dp :
            dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
    print(dp[num])

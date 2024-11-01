# 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
# N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
# i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.

# dp인가.. 백트래킹인가, bfs인가.. dp 같다.. 왜냐면 내 위에랑만 다르면 됨
#  n이 1000
import sys
n = int(sys.stdin.readline())
dp={}
# 1줄 밖에 없으면 그줄 최소값
# 2줄부터는

for _ in range(0,n):
    start,mid,end = map(int,sys.stdin.readline().split())
    if _ == 0 :
        dp[1],dp[2],dp[3] = start,mid,end
        continue
    temp1 = min(dp[2]+start,dp[3]+start)
    temp2 = min(dp[1]+mid,dp[3]+mid)
    temp3 = min(dp[1]+end,dp[2]+end)
    dp[1],dp[2],dp[3] = temp1,temp2,temp3

print(min(dp.values()))



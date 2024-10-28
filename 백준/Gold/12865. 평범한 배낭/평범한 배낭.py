# 첫줄에 물품의 수 , 준서가 버틸 수 있는 무게가 주어짐
import sys
temp_list = []
n, k = map(int, sys.stdin.readline().split())
# print(n,k)

for i in range(n):
    w,v = map(int,sys.stdin.readline().split())
    temp_list.append([w,v])

temp_list.sort(key=lambda x:(x[0],x[1]))
# print(temp_list)

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
# print(dp)
for i in range(1,n+1):
    for j in range(1,k+1):
        if j >= temp_list[i-1][0] :
            dp[i][j] = max(temp_list[i-1][1]+dp[i-1][j-temp_list[i-1][0]],dp[i-1][j])
        else :
            dp[i][j] = dp[i-1][j]
print(dp[n][k])
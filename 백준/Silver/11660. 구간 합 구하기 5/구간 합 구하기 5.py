import sys
'''
n*n 정사각형
첫 번째 줄은 n, m
n은 정사각형 길이, m은 m번의 (x1,y1) (x2,y2)를 표현


오른쪽 -> 가면서 내 전까지 누적합을 구해놓기
내려가면서 내 전까지 누적합을 구해놓기



11 11+12 11+12+13 11+12+13+14
11+21 11+12+21+22

22 ~ 34 => 22+23 + 32+33+ 42+43

는 오른쪽 누적합(dp)은 나는 =>나 + 나의 위 + 나의 왼쪽 옆 -나의 왼쪽 대각선위

'''

n,m = map(int, sys.stdin.readline().split())
# print(n,m)


sq=[]
for _ in range(n):
    sq.append(list(map(int,sys.stdin.readline().split())))
# print(sq)

dp = [[0] * (n+1) for _ in range(n+1)]
# print(dp)
for i in range(1,n+1):
    for j in range(1,n+1):
        dp[i][j] = dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]+sq[i-1][j-1]
# print(dp)


for _ in range(m):
    x1,y1,x2,y2 =map(int,sys.stdin.readline().split())
    print(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1])
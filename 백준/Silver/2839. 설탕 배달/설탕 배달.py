'''
3kg, 5kg

최대한 적은 봉지로 가져가야 한다.

N kg를 가져가려 한다.
3 3
4    x
5 (5)
6 (3,3)    dp[3]  dp[1] 만약에 없으면 5000을 주자..
7 (x)
8 (3,5)
9 (3,3,3)
10 (5,5)
11 (3 3 5)
12 ( 3,3,3,3)
13 (3,5,5)
14 (3 3 3 5)
15 (5,5,5)


4,7 제외하면 다 있다..

알고리즘 분류 : DP?
어떻게 풀이?

dp[i] = min(dp[i-3],dp[i-5])+1
'''

import sys
input = sys.stdin.readline
dp = {3:1,4:5000,5:1}

n = int(input())
for i in range(6,n+1):
    left = 5000
    right = 5000
    if   i-3 in dp  :
        left = dp[i-3]
    if   i-5 in dp :
        right = dp[i-5]
    dp[i] = min(left,right) + 1

if dp[n]>=5000 :
    print(-1)
else :
    print(dp[n])
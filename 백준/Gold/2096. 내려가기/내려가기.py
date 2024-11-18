'''
N줄에 0 이상 9 이하의 숫자가 세 개씩 적혀 있다.
시작 : 첫 줄
끝 : 마지막 줄
ex ))
3
1 2 3
4 5 6
4 9 0

문제 이해하기 : 먼저 처음에 적혀 있는 세 개의 숫자 중에서 하나를 골라서 시작하게 된다.

그리고 다음 줄로 갈 떄의 제약 조건
1) 바로 아래
2) 바로 아래와 붙어 있는 곳

2가지로만 내려 갈 수 있음.

최소, 최대 점수를 구하자


알고리즘 분류 : 첫 번째줄이 다음줄에 영향을 줌 -> DP

어떻게 풀이?
1번째 줄이 3,5,8이고
2번 째 줄이 1,2,3이라 하면 첫 번째 1은 3,5의 최대 + 나(1), 2는 3,5,8중 최대 + 나(2)...
이런 식으로 한 줄 한 줄 갈 때마다 최대값이 이미 정해짐..

'''
import sys

n = int(sys.stdin.readline())

dp= {1:0,2:0,3:0}
dp_min = {1:0,2:0,3:0}
for _ in range(n):
    a,b,c = map(int, sys.stdin.readline().split())
    if _ == 0 :
        dp[1],dp[2],dp[3] = a,b,c
        dp_min[1],dp_min[2],dp_min[3] = a,b,c
        continue
    temp1 = max(dp[1], dp[2]) + a
    temp2 = max(dp[1], dp[2], dp[3]) + b
    temp3 = max(dp[2], dp[3]) + c

    tmp1 = min(dp_min[1], dp_min[2]) + a
    tmp2 = min(dp_min[1], dp_min[2], dp_min[3]) + b
    tmp3 = min(dp_min[2], dp_min[3]) + c


    dp[1] = temp1
    dp[2] = temp2
    dp[3] = temp3

    dp_min[1] = tmp1
    dp_min[2] = tmp2
    dp_min[3] = tmp3

print(max(dp.values()),end=" ")
print(min(dp_min.values()))
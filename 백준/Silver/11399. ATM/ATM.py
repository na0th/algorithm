'''
ATM 1대, [1,2,3,4,5] 같이 리스트가 주어짐
각 사람이 돈을 뽑는데 걸리는 시간..
전부의 Waiting Time을 최소로 해야 함.


알고리즘 분류 : 그리디
어떻게 풀이 ?
전부의 waiting time을 최소화 하려면
소요 시간이 적은 사람이 먼저..
그냥 오름차순 정렬하면 된다..!!

'''

import sys

n = int(sys.stdin.readline())

times = list(map(int, sys.stdin.readline().split()))

times.sort()
# 1 2 3 3 4
# 1 12 123 1233 12334

# 1* 5  5
# 2* 4 8
# 3* 3  9
# 3* 2 6
# 4* 1  4
total = 0
for idx,time in enumerate(times):
    total +=  (n-idx)*time
print(total)
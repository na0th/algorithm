'''
산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값
범위 : N개의 수들 중 최댓값과 최솟값의 차이

4개를 구하시오.

첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
둘째 줄에는 중앙값을 출력한다.
셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
넷째 줄에는 범위를 출력한다.


알고리즘 분류 : 구현
어떻게 풀이?

1 : 산술평균은 sum, 소수점 반올림
2 : 중앙값은 sort()후 중간 인덱스 반환
3: 가장 많이 나타나는 값은 딕셔너리에 값 넣고 반환
4 : max - min
'''

import sys
from collections import defaultdict
from collections import Counter
input = sys.stdin.readline

n = int(input())


num_list = []
for _ in range(n):
    num = int(input())
    num_list.append(num)

#1
print(round(sum(num_list)/n))
# 2
num_list.sort()
idx = n//2
print(num_list[idx])

#3
count = Counter(num_list)
most_common = count.most_common()
most_common.sort(key=lambda x: (-x[1], x[0]))

if len(most_common) > 1 and most_common[0][1] == most_common[1][1]:
    mode = most_common[1][0]
else:
    mode = most_common[0][0]
print(mode)
# 4
print(max(num_list)-min(num_list))
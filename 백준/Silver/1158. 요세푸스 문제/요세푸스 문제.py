'''
4:35분 시작

1번부터 N번까지 원으로 앉는다.
순서대로 K번째 사람을 제거한다.
N명을 제거할 때까지 계속한다.
예시 (7,3) = [3,6,2,7,5,1,4]

1<= K <=N <= 5000

1,2,3,4,5,6,7 => 3
4,5,6,7,1,2 => 6
7,1,2,4,5 => 2
4,5,7,1 => 7
1,4,5 => 5
1,4 => 1 (1,4,1)
4 => 4 (4,4,4)

알고리즘 분류 : 수학(나머지)? , 큐 ?
어떻게 풀이 :
수학 풀이 ->
N(변하는 수)을 K로 나눈 나머지 인덱스에 해당하는 사람 제거
'''

import sys

n, k =  map(int,sys.stdin.readline().split())

result = []
people = list(range(1, n + 1))
idx = 0

while people:
    idx = (idx + k - 1) % len(people)
    result.append(people.pop(idx))

print(f"<{', '.join(map(str, result))}>")
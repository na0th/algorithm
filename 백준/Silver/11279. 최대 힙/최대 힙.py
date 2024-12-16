'''

배열에 자연수 x를 넣는다.
배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.

첫째 줄에 연산의 개수 N(1 ≤ N ≤ 100,000)이 주어진다.
다음 N개의 줄에는 x가 주어진다.
x가 자연수라면 배열에 x라는 값을 넣는다
x가 0이라면 가장 큰 값을 출력하고 그 값을 배열에서 제거


0인데, 빈 배열이면 0 출력

알고리즘 분류 : 최대 힙
어떻게 풀이?
최소힙을 반대로 풀기(-를 넣는다)
'''

import sys
import heapq
n = int(sys.stdin.readline())


pq = []

for _ in range(n):
    num = int(sys.stdin.readline())
    if num != 0 :
        heapq.heappush(pq,(-num))
    else :
        if pq :
            pick = heapq.heappop(pq)
            print(-pick)
        else :
            print(0)
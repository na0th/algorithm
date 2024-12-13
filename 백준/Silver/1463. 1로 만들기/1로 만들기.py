'''
정수 X에 사용할 수 있는 연산은 3가지

1) X가 3으로 나누어 떨어지면, 3으로 나눔
2)X가 2로 나누어 떨어지면, 2로 나눔
3)1을 뺀다.
정수 N이 주어질 때 1로 만드는 최소 횟수


알고리즘 분류 : 최소 횟수? BFS ? 최소 힙?

어떻게 풀이?


queue에 1인 경우, 2인 경우, 3인 경우 다 넣는다. 계속 뽑아서 1인지 확인 아니라면 넣음
최소 힙을 써볼까? -> 작은 수일수록 1이 빨리 나오지 않을까..

'''

import sys
from collections import deque
import heapq
n = int(sys.stdin.readline())

pq = []
heapq.heappush(pq,(0,n))
visited = set()
while pq:
    cnt, cur_num  = heapq.heappop(pq)

    if cur_num in visited:
        continue
    visited.add(cur_num)

    if cur_num == 1 :
        print(cnt)
        break
    if cur_num % 3 == 0 :
        heapq.heappush(pq,(cnt+1,cur_num//3))
    if cur_num % 2 == 0:
        heapq.heappush(pq,(cnt+1,cur_num//2,))

    heapq.heappush(pq,(cnt+1,cur_num-1))


'''

상근이는 새로 프린터기의 소프트웨어 개발했다.

1. 현재 Queue의 가장 앞에 있는 문서의 중요도를 확인한다.
2. 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면
이 문서를 인쇄하지 않고, Queue의 가장 뒤에 재배치한다. 그렇지 않으면 인쇄한다.

4개의 문서  A,B,C,D가 있고, 중요도가 2-1-4-3이라면 C를 인쇄하고, D를 인쇄하고, A,B를 인쇄한다.
중요도는 1~9까지로 중요도가 같을 수 있다.

결국, 가장 큰 수면 출력하고 아니면 맨뒤로 보낸다.. 맨뒤로 보내는 건 의미 없지않나..
heap으로 하고 싶어도 뒤로 보낸 순서가 있어서 안되겠다..

queue랑 heap을 같이 써본다면??

알고리즘 분류: Queue, heap?
어떻게 풀이 ?
heap에 queue element를 넣음
queue를 돌면서 heap을 뒤져서 heappop한 것이랑 queue element를 비교해서..
queue element가 크거나 같다면 queue에서는 빼고, heap에서도 뺀다
[
문서의 개수, 궁금한 문서 인덱스
문서들의 중요도들
] 위의 꼴로 주어짐.
'''
import sys
import heapq
from collections import deque
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    doc_n, find_doc_idx = map(int,input().split())
    nums = list(map(int,input().split()))

    queue = deque(enumerate(nums))
    heap = [-priority for priority in nums]
    heapq.heapify(heap)

    cnt = 0
    while queue :
        idx, priority = queue.popleft()

        if priority <-heap[0]:
            queue.append((idx, priority))

        else :
            heapq.heappop(heap)
            cnt +=1
            if idx == find_doc_idx:
                print(cnt)
                break

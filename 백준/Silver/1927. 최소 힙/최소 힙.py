'''

최소 힙

자연수면 ,배열에 자연수 x를 넣는다.
0이면 ,배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.


첫째 줄에 연산의 개수 N
다음 N개의 줄에는 x가 자연수라면 배열에 x라는 값 추가
x가 0이라면 배열에서 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우이다.
x는 2^31보다 작은 자연수 또는 0이다.

입력에서 0이 주어진 횟수만큼 답을 출력한다.
만약 배열이 비어 있는 경우인데 가장 작은 값을 출력하라고 한 경우에는 0을 출력하면 된다.


알고리즘 분류 : 최소 힙?
어떻게 풀이 ?  :
최소 힙써서 0나오면 heappop하고
x나오면 x heappush



'''
import sys
import heapq

n = int(sys.stdin.readline())

pq = []
for _ in range(n):
    num = int(sys.stdin.readline())
    if num == 0 :
        if pq :
            pick = heapq.heappop(pq)
            print(pick)
        else :
            print(0)

    else :
        heapq.heappush(pq,num)

'''
첫 줄에는 N번째 큰 수
N^2의 수가 주어진다.

알고리즘 분류 : 정렬(X) -> 시도해봤는데 메모리 초과
heap
어떻게 풀이? 정렬해서 리턴? -> 메모리 초과
heap 구조로 n개의 값만 추적해본다.


'''
import sys
import heapq
input = sys.stdin.readline

n = int(input())

pq = []
for _ in range(n):
    nums = list(map(int, input().split()))
    for num in nums :
        if len(pq) <n :
            heapq.heappush(pq,num)
        else :
            min_num = heapq.heappop(pq)
            if num >= min_num :
                heapq.heappush(pq,num)
            else:
                heapq.heappush(pq,min_num)

print(pq[0])
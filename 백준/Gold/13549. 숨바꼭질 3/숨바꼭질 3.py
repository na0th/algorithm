import sys

n,m = map(int, sys.stdin.readline().split())

# print(n,m)

'''
n과 m이 주어지는데, n -> m 으로 가는 최소 횟수 구하기
1초 후에 X-1 or X+1 이거나
0초 후에 2*X로 이동

문제 설명 : 윗부분 참조
알고리즘 분류 : 최소 횟수 -> BFS?
어떻게 풀이?
queue에다 3가지 경우를 다 넣는다 그래서 m이 되면 return 한다
근데 이렇게 하면 순간이동 때문에 count가 망가지니까 우선순위 큐로 최소 횟수를 보장하자..
'''
import heapq
pq = []
visited = set([n])

heapq.heappush(pq,(0,n))

answer = -1
while pq:
    count,cur_position = heapq.heappop(pq)

    if cur_position == m :
        answer = count
        break

    for next_count,next_position in [(count,cur_position*2),(count+1,cur_position+1),(count+1,cur_position-1)]:
        if 0 <= next_position <= 2 * max(n,m) and next_position not in visited:
            visited.add(next_position)
            heapq.heappush(pq,(next_count,next_position))




print(answer)
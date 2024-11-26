'''
문제 요약 :

수빈 N, 동생 K
 걷는다 => 1초 후에 X-1 OR X+1로 이동
 순간이동 => 1초 후에 2*X로 이동

가장 빨리 찾는 시각 몇 초..?
가장 빠른 시간으로 찾는 방법이 몇 가지?

알고리즘 분류 : 우선순위큐와 BFS?

어떻게 풀이?
가장 빨리 찾는 건 우선순위큐..? 구했음..

가장 빠른 시간으로 찾는 방법은 ?? 빠른 시각을 아니까 그걸 기반으로 DFS?? BFS??


'''
import sys
import heapq
from collections import deque
n, k = map(int, sys.stdin.readline().split())

# print(n,k)


def cal_time(start,end):
    visited = set([start])
    pq = []
    heapq.heappush(pq,(0,start))

    while pq :
        count, cur_position = heapq.heappop(pq)

        if cur_position == end :
            return count

        for next_count,next_position in ((count+1,cur_position-1),(count+1,cur_position+1),(count+1,cur_position*2)):

            if 0 <= next_position <= 2*max(n,k) and next_position not in visited:
                visited.add(next_position)
                heapq.heappush(pq,(next_count,next_position))


min_time = cal_time(n,k)
print(min_time)



def bfs(n,k,min_time):
    max_pos = 100001
    queue = deque([(n,0)])
    cnt = 0
    visited = [float('inf')] * max_pos
    while queue :
        cur_pos, cur_time = queue.popleft()

        if cur_time > min_time :
            break

        if cur_pos == k:
            if cur_time == min_time :
                cnt+=1
            continue

        for pos in ((-1,1,cur_pos)):
            next_pos = cur_pos+pos
            if 0 <= next_pos < max_pos and cur_time+1 <=visited[next_pos] :
                visited[next_pos] = cur_time + 1
                queue.append((next_pos,cur_time+1))

    return cnt


print(bfs(n,k,min_time))

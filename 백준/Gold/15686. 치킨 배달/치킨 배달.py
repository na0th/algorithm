'''
치킨 거리는 집과 가장 가까운 치킨집 사이의 거리이다
도시의 치킨 거리는 모든 집의 치킨 거리의 합이다.

임의의 두 칸 (r1, c1)과 (r2, c2) 사이의 거리는 |r1-r2| + |c1-c2|로 구한다.

치킨집을 m개만 남길 것.
어떻게 골라야 도시의 치킨 거리가 최소가 될지?
0은 빈 칸, 1은 집, 2는 치킨집을 의미한다
집의 개수는 2N개를 넘지 않으며, 적어도 1개는 존재한다.
치킨집의 개수는 M보다 크거나 같고, 13보다 작거나 같다.

알고리즘 분류 : 어떤 방법이 있는 건가? 무작정 완전탐색이 아니려나..?


어떻게 풀이?
그냥 완전탐색이면  집은 100개 가능, 치킨집은 13까지 가능
최악의 경우 13C6 * 100인데 ..  170,000 이정도면 괜찮음

'''

import sys
n,m = map(int,sys.stdin.readline().split())

graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
# print(graph)

home = list()
chicken = list()
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            home.append((i,j))
        elif graph[i][j] == 2:
            chicken.append((i,j))
#DFS나 combinations 쓰거나

result = []
def dfs(visited,count,idx):
    if count == m :
        #home과의 거리 계산해서 더하기
        chicken_dist = 0
        for hx,hy in home:
            min_dist = float('inf')
            for cx,cy in visited:
                distance = abs(hx-cx)+abs(hy-cy)
                min_dist = min(min_dist,distance)
            chicken_dist += min_dist

        result.append(chicken_dist)
        return

    for i in range(idx, len(chicken)):
        visited.append(chicken[i])
        dfs(visited,count+1,i+1)
        visited.pop()

dfs([],0,0)
print(min(result))
# print(home)
# print(chicken)

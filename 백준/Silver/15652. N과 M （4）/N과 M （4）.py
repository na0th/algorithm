'''
문제 요약 :
1부터 N까지 자연수 중에서 M개를 고른 수열
같은 수 중복 ok , 비내림차순
길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

알고리즘 분류 : 백트래킹?

어떻게 풀이?
나보다 크거나 같으면 계속 진행
그러다 count가 m개가 되면 출력

'''
import sys

n,m = map(int,sys.stdin.readline().split())
# print(n,m)

def backtrack(visited,count,start):
    if count == m :
        print(*visited)
        return
    for i in range(start,n+1,1):
        visited.append(i)
        backtrack(visited,count+1,i)
        visited.remove(i)
visited = []

backtrack(visited,0,1)



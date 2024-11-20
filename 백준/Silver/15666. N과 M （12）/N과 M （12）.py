import sys

n,m = map(int,sys.stdin.readline().split())

num_list = sorted(map(int,sys.stdin.readline().split()))

result = set()
def backtrack(visited,count,start):

    if count == m :
        result_tuple = tuple(visited)
        if result_tuple not in result:
            result.add(result_tuple)
            print(*visited)
        return

    for i in range(start,n,1):
        visited.append(num_list[i])
        backtrack(visited,count+1,i)
        visited.pop()

visited = []
backtrack(visited,0,0)
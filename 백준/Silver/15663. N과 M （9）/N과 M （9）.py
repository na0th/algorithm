import sys
import copy

n,m = map(int,sys.stdin.readline().split())

numbers = list(map(int,sys.stdin.readline().split()))
numbers.sort()

result = set()
def backtrack(visited,numbers,cnt):

    if cnt == 0 :
        if tuple(visited) not in result :
            result.add(tuple(visited))
            print(*visited)
        return

    for i in range(len(numbers)):
        visited.append(numbers[i])
        backtrack(visited,numbers[:i] + numbers[i+1:] ,cnt-1)
        visited.pop()

visited =  []
backtrack(visited,numbers,m)

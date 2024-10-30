import sys

n, m = map(int, sys.stdin.readline().split())

# 백트래킹
nums = [i+1 for i in range(n)]
# print(nums)

def backtrack(nums, visited, pick_count,start):
    if pick_count == 0 :
        for num in visited:
            print(num, end=' ')
        print()
        return
    for i in range(start,n) :
        if nums[i] not in visited:
            visited.append(nums[i])
            backtrack(nums,visited,pick_count-1,i+1)
            visited.remove(nums[i])
    return visited
visited = []
backtrack(nums,visited,m,0)

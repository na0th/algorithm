'''
경래는 n개의 달걀을 갖고 있음.
잠재 고객은 m명, i번째 고객은 달걀 하나를 P[i] 가격 이하로 살 수 있다고 말함.
한 고객에게 1개만 판다..
A가격에 팔면, P[i]가 A 가격보다 크거나 같은 모든 고객은 달걀을 산다..
최대 수익을 올릴 수 있는 가장 낮은 달걀의 가격 책정?

P가 10^6..
nlogn 이하만..

알고리즘 분류 : 정렬, 수학?
어떻게 풀이?
정렬해서, nums[idx] * n-idx의 최대값


'''
import sys
input = sys.stdin.readline

n,m = map(int, input().split())

nums = []
for _ in range(m):
    nums.append(int(input()))


nums.sort()
result = []
for idx, num in enumerate(nums):
    eggs_sold = min(n, m - idx)

    result.append(num*(eggs_sold))

value_idx = result.index(max(result))
print(nums[value_idx], max(result))


'''
N개로 된 수열 A[0].. A[N-1]가 있다.
1 <= N <= 10000
I번째부터 J번째 까지 합이 M이 되는 경우의 수를 찾으시오

알고리즘 분류 : DP? N이 작으니까 완전탐색도 가능한가? X.. nlogn까지만 가능하다..
어떻게 풀이?
1) 완전탐색 O(N^2) = 1억번.. 안된다..
2) DP?


누적합을 구한다.. 그것은 처음부터 나까지의 합, 근데 1~5의 합이 15면, 1~1 빼면 2~5까지다
1~2빼면 3~5까지다. 1~3빼면 4~5까지다.
그걸 다 해서 구하면 되지 않을까..-> o(n^2) => 안됨..



'''
from collections import Counter
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
nums = list(map(int,input().split()))

prefix_sum = [0] * (n + 1)
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

sum_count = Counter()
sum_count[0] = 1
count = 0

for i in range(1,n+1):
    target = prefix_sum[i]-m
    count += sum_count[target]
    sum_count[prefix_sum[i]] += 1

print(count)
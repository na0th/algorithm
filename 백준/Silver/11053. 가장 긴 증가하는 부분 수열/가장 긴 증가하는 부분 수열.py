import sys
from collections import defaultdict
num = int(sys.stdin.readline())

# print(input)
num_list = list(map(int, input().split()))
# print(num_list)
dp = [1]*len(num_list)
for i in range(1,len(num_list)):
    for j in range(i):
        if num_list[j] < num_list[i] :
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))
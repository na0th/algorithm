'''
N개의 카드
맨 앞에 버리고 = 234
맨 앞에 거를 맨아래로 내려 = 342

알고리즘 분류 : 큐
어떻게 풀이 ?

큐로 넣고 내려
'''
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
num_list = deque(i+1 for i in range(n))

# print(num_list)
while num_list :
    pop = num_list.popleft()
    print(pop,end=" ")
    if not num_list:
        break
    pop_2 = num_list.popleft()
    num_list.append(pop_2)

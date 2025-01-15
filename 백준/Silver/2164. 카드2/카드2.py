'''
제일 위에 1, 제일 아래에 N이 있다.
카드가 한 장 남을 때까지 반복.
제일 위에 있는 카드를 버린다. 그다음 제일 위에 있는 카드를 맨뒤에 놓는다.

시작 1234 -> 234 -> 마무리 342

이렇게 계속 반복함..

알고리즘 분류: 큐
어떻게 풀이? 큐 구현

'''
import sys
input = sys.stdin.readline()
from collections import deque
n = int(input)

nums = deque([_+1 for _ in range(n)])

for i in range(n-1):
    nums.popleft()
    pop = nums.popleft()
    nums.append(pop)
print(nums[0])
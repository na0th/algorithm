'''
N명의 참가자.. 1번부터 N번까지

인접한 번호끼리 게임
홀수면 마지막 번호는 자동 진출

A,B의 번호가 주어졌을 때, 몇라운드에서 만나는 지 출력하시오
둘은 항상 이긴다.

서로 대결하지 않을 때는 -1을 출력..

N은 10^6

1,2
0..0
0...1

1..0
1..1

3,4가 있음..
5 6
7 8

1 3 5 7 올라감
10 - 5 - 2..1 -> 1
15..1 - 7..1-> 3- 1


알고리즘 분류 : 수학
어떻게 풀이 ?
그냥 전 라운드에서 1명만 올라왔다고 가정함
그럼 맨처음에 20번이면
이번라운드에서는 나까지 10명이고, 난 10등
그럼 다음 라운드는 나까지 5명이고, 난 5등

맨처음에 31이면 +1해서 32명이고
이번 라운드는 나까지 16등..??
다음 라운드는 나까지 8등..


10 5 3 2
16 8 4 2

결국 나에서 +1 해서 /2 한 숫자가 같아지는 시점이 언제인지?

'''

import sys
input = sys.stdin.readline

n, a, b = map(int,input().split())
cnt=1
while(True):
    if (a+1)//2 != (b+1)//2 :
        a=(a+1)//2
        b=(b+1)//2
        cnt+=1
    else :
        print(cnt)
        break
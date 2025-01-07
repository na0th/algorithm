'''
첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다.
다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다.
다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다.
다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다.

2번째 줄에 A = [4,1,5,2,3]
그리고 5개의 수들 = [1,3,7,9,5]가 각각 A안에 존재하면 1 아니면 0을 출력한다.

알고리즘 분류 : 해시
어떻게 풀이?
A에 포함되는 수들을 딕셔너리에 넣는다.
그리고 M개의 수들을 각각 딕셔너리에 존재하지는지 아닌지로 1, 0 을 출력한다.
'''
import sys
input = sys.stdin.readline

n = int(input())
dic = dict()
A = list(map(int, input().split()))
for item in A :
    dic[item] = 1
m = int(input())
numbers = list(map(int, input().split()))
for number in numbers :
    if number not in dic :
        print(0)
    else :
        print(1)
# print(A)
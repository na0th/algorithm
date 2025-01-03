'''
1번 - 2번 -3번 ... n번 -1번 이렇게 원 형태

주어지는 건 1,2번 합 2,3번 합 ... n,1번 합이 주어짐

그 때 번호들의 숫자를 구하시오.
N은 999명 이하의 홀수..
알고리즘 분류 : 백트래킹? 하다가 안되면 돌아온다? 숫자가 작으니까 완전탐색?
어떻게 풀이 :
딕셔너리로 백트래킹?
2중 for문?
'''
N = int(input())
sums = [int(input()) for _ in range(N)]


first = 0
for i in range(len(sums)):
    if i%2 == 0 :
        first+=sums[i]
    else :
        first-=sums[i]

first = first//2

k = first
result = [first]
for i in range(N - 1):
    next_num = sums[i]-k
    result.append(next_num)
    k = next_num



for candy in result:
    print(candy)
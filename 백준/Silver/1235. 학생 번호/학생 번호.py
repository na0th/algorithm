'''
학생 번호가 주어진다.
맨뒤에서부터 1글자씩 늘려가면서 서로가 구분이 되는 숫자가 되면 된다.
1212345
1212356
0033445

1글자면 5 6 5라 겹침
2글자면 45 56 45 라 겹침
3글자면 345 356 445라 안겹침

학생 수  1<= n <= 1000
문자열의 길이 m <= 100

알고리즘 분류 : 완전탐색? -> n,m이 작으니까
어떻게 풀이 ?

리스트에 i개를 뽑아서 넣는다. 학생 문자열 맨뒤에서 1개부터.. 늘려가면서..
다 넣은 후에 len() 해서 n 맞는지 검사


'''
import sys
input = sys.stdin.readline

n = int(input())

numbers = []
for _ in range(n):
    numbers.append(input().strip())

back_idx = 1
while True:
    suffixes = [num[-back_idx:] for num in numbers]
    if len(suffixes) == len(set(suffixes)):
        print(back_idx)
        break
    back_idx += 1
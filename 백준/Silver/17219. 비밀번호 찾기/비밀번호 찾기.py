'''
사이트주소 : 비밀번호
key : value 쌍

n m이 주어지면
딕셔너리 element 개수, 찾아야 하는 사이트 비밀번호 수를 의미

알고리즘 분류 : 해시 맵, 딕셔너리
어떻게 풀이?
그냥 딕셔너리에 다 넣고, key로 value 찾으면 된다

'''

import sys

n,m = map(int, sys.stdin.readline().split())

dic = {}
for _ in range(n):
    site, password = sys.stdin.readline().split()
    dic[site] = password

for i in range(m):
    site = sys.stdin.readline().strip()

    print(dic[site])
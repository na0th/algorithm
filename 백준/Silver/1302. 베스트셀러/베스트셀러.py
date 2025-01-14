'''
팔린 책 목록이 주어질 때, 가장 많이 팔린 책을 출력
같으면, 사전 순으로 가장 앞선 책 출력


알고리즘 분류 : 해시, 정렬?
어떻게 풀이?
책 이름을 key로 적고, value로 있으면 카운팅
가장 많이 뽑힌 거 추려서.. 정렬하기기
'''

import sys
input = sys.stdin.readline

from collections import defaultdict

n = int(input())

dic = defaultdict(int)
for _ in range(n):
    book = input().strip()
    dic[book]+=1

max_count = max(dic.values())
most_sold_books = [k for k, v in dic.items() if v == max_count]

print(sorted(most_sold_books)[0])
# print(dic)

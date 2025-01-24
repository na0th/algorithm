'''
숫자 카드 N개, 정수 M개가 주어지면
숫자 M개의 숫자중, 갖고 있는 숫자 카드 갯수를 구하시오

알고리즘 분류 : 딕셔너리(해시)
어떻게 풀이?
딕셔너리에 넣고 값 찾아주면 됨..

'''

import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
dic = defaultdict(int)
m_nums =list(map(int,input().split()))
for m_num in m_nums :
    dic[m_num]+=1
n = int(input())
n_nums = list(map(int,input().split()))
for n_num in n_nums :
    print(dic[n_num],end=" ")
# print(dic)
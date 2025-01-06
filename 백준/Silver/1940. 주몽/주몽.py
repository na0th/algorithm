'''
두 재료의 고유한 번호를 합쳐서 M(1<= M <= 10000)이 되면 갑옷이 됨

갖고 있는 재료로 최대 갑옷 갯수 출력

알고리즘 분류 : two sum? 해시?
어떻게 풀이?
value = m - key
만족하는 value가 있는지 확인한다
'''
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

dic = dict()

nums = list(map(int,input().split()))

for item in nums :
     dic[item] = m - item

cnt = 0
for value in dic.values():
    if value in nums :
       cnt+=1

print(cnt//2)
'''
 한번 입었던 옷들의 조합을 다시 입지 않는다.
예를 들어 오늘 안경, 코트, 상의, 신발을 입었다면,
다음날은 바지를 추가로 입거나 안경대신 렌즈를 착용하거나 해야한다.

모두 착용 안하는 경우는 X

알고리즘 분류 : 조합? 딕셔너리?
어떻게 풀이?
카테고리를 분류해서, 전부 안 입는 경우를 뺌..

HEADGEAR : 3
FACE : 2
EYEWEAR : 3이라 하면

(3+1)*(2+1)*(3+1) -1 ?
+1 해서 다 곱해서 -1..하기 !
왜?
카테고리에서 선택을 안 하는 경우의 수 +1 해줘야 함.. 그렇지만 전부 다 안입으면 안되니 -1

결국 카테고리 별로 몇 개의 Element가 있는지만 구하면 됨
'''
import sys
from collections import defaultdict
n = int(sys.stdin.readline())



for _ in range(n):
    m = int(sys.stdin.readline())
    dic = defaultdict(list)
    for j in range(m):
        element , category = list(sys.stdin.readline().split())
        dic[category].append(element)

    total = 1
    for k,v in dic.items() :
        total = total * (len(v)+1)
    total-=1
    print(total)



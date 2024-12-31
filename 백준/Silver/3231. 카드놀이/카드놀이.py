'''
1~N 카드
맨처음부터 1 보이면 뽑음 그자리부터 2를 찾음
맨 끝에 도달하면 박수침, 그리고 다시 맨 처음부터 ..


박수친 횟수를 출력
일단 N은 최대 10만..

알고리즘 분류 : 해시?, 그리디?
어떻게 풀이?

만약에 처음 돌면서 모든 값의 인덱스를 찾아놓는다면?
1은 그냥 찾았다 가정
2부터는 i-1 인덱스보다 i의 인덱스가 크면 그냥 넘어감, 작으면? cnt+1


'''
import sys
n = int(sys.stdin.readline())

dic = dict()
for i in range(n):
    num = int(sys.stdin.readline())
    dic[num]=i+1


cnt = 0
current = dic[1]
for k in range(2,n+1):
    if dic[k] < current :
        cnt+=1
    current = dic[k]
print(cnt)
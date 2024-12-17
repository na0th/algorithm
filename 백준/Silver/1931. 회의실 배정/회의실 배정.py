'''
회의 시작, 끝 시간이 주어짐
끝나자마자 동시에 시작할 수 있음.
최대로 회의에 참여할 수 있는 수 출력하기


알고리즘 분류 :  greedy
어떻게 풀이?
회의 끝나는 시각 순으로 정렬함
제일 빨리 끝나는 것부터 greedy하게 고른다
그대신 끝마친 시각보다 시작 시간보다 작은 건 패스..
-> 4초에 끝났는데 (3,5)면 패스스
ex) 1 4 / 5 7 / 8 11/ 12 14
'''
import sys

n = int(sys.stdin.readline())

time_list = []
for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    time_list.append([start,end])

time_list = sorted(time_list, key= lambda x:(x[1],x[0]))
# print(time_list)

result = []
end_time = 0
for item in time_list :
    start, end = item
    if start >= end_time :
        result.append(item)
        end_time = end

print(len(result))



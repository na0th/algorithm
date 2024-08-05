def solution(routes):
    '''
    정렬 시키고 맨 마지막에 꽂기 
    찍히는 차들은 빼기
    '''
    from collections import deque
    routes.sort(key=lambda x:-x[1])
    stack = list(routes)
    print(stack)
    cnt = 0
    while (stack) :
        pop = stack.pop()
        while(stack and stack[-1][0] <= pop[1]):
            stack.pop()

        cnt += 1
    return cnt
#     print(routes)
#     answer = 0
#     return answer
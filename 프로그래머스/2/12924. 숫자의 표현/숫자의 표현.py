def solution(n):
#   연속합을 .. 어떻게..
#   내가 홀수? 내가 짝수? // 개수가 짝수? 홀수?
#   시그마 개념으로 접근해서 (j(j+1)-i(i+1))/2 = n 방정식 풀기

#  정답은 나오는데, 효율성에서 탈락..
#     cnt=0
#     for i in range(0,n+1):
#         for j in range(i+1,n+1):
#             if j*(j+1)-(i)*(i+1) == 2 * n :
#                 cnt+=1

#     return cnt
    cnt = 0
    i = 1
    j = 1
    current_sum = 0

    while i <= n:
        if current_sum == n:
            cnt += 1
            current_sum -= i
            i += 1
        elif current_sum < n:
            current_sum += j
            j += 1
        else:
            current_sum -= i
            i += 1

    return cnt
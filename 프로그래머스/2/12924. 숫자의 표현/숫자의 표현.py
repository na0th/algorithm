def solution(num):
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

    answer = 0
    for x in range(1,num+1):
        sum = 0
        for y in range(x, num+1):
            sum += y
            if sum == num:
                answer += 1
                break
            elif sum > num:
                break

    return answer
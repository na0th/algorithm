def solution(n):
    dic = {0:1,1:1}
    for i in range(2,n+1):
        if i not in dic :
            dic[i] = dic[i-1]+dic[i-2] %1234567
    
    answer = dic[n-1] % 1234567
    return answer
def solution(n):
    dic = {2:3,4:11}
    for i in range(3,n+1):
        if i % 2 == 1 :
            dic[i] = 0
        else :
            if i-2 in dic and i-4 in dic :
                dic[i] = (4*dic[i-2]-dic[i-4])%1000000007
        
    answer = dic[n]%1000000007
    return answer

print(solution(6))


def solution(n):
    arr = [1 for i in range(n+1)]
    for k in range(2,n):
        j = 2
        while(k*j <=n) :
            if arr[k*j] == 1 :
                arr[k*j] = 0
            j+=1

    answer = arr.count(1)-2
    return answer
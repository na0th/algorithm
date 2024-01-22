def solution(n, m):
#  최대 공약수 .. 
#  최소 공배수..

#   나눠서 서로소를 만들어야 한다..
    max_idk = 1
    min_idk = 1

    i = 2
    while(1):
        if n % i == 0 and m % i == 0 :
            max_idk = max_idk * i
            min_idk = min_idk * i
            
            n = n // i
            m = m // i
            
            i = 1
        else : 
            if i >= max(n,m) :
                min_idk = max_idk * n * m
                break
        i+=1
    answer = []
    answer.append(max_idk)
    answer.append(min_idk)
    return answer
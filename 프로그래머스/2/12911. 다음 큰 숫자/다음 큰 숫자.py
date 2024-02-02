def solution(n):
    count_one = str(bin(n)[2:]).count('1')
    
    i = n+1
    while(1):
        if str(bin(i)[2:]).count('1') == count_one :
            print(i)
            break
        i += 1
        
    answer = i
    return answer
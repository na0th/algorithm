def solution(prices):
    answer = []
    for i in range(len(prices)):
        num = prices[i]
        check = -1
        for j in range(i+1,len(prices)):
            if num > prices[j] :
                check = 1
                answer.append(j-i)
                break
        if check == -1 :
            answer.append(len(prices)-1-i)
                
            
    return answer
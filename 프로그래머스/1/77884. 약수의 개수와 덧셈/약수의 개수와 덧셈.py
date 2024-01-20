def solution(left, right):
#   방법이 있나.. 그냥 해야지
    def count_divisor(num) :
        cnt = 0
        for i in range(1,num+1):
            if num % i == 0:
                cnt+=1
        return cnt
    
    answer = 0
    for i in range(left,right+1) :
        # print(count_divisor(i))
        if count_divisor(i) % 2 == 0:
            answer+=i 
        else :
            answer-=i
    
    return answer
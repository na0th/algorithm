def solution(n, k):
    import math

# 소수 판별 함수
    def prime_number(x):
        if x < 2 :
            return False
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False 
        return True 

    # def prime_number(num) :
    #     if num < 2 :
    #         return False
    #     for i in range(2,num):
    #         if num % i == 0:
    #             return False
    #     return True
        
#   일단 n진법 변환하기
    def n_trans(num):
        string = ""
        while(num >= k):
            mod = num % k
            num = num // k 
            string += str(mod)
            
        string+= str(num)
        return string[::-1]
    
    # print(n_trans(n))
    im = n_trans(n)

#   0을 기준으로 자르기// 만약 0이 없다면?
    # if im.count('0') == 0 :
    #     if prime_number(im) == True :
    #         return 1
    #     else :
    #         return "0"
    
    split = im.split('0')
#   공백 걸러내기(문법 외워)
    split = [i for i in split if i.isdigit()]
    
    # print(split)
#  소수 판별 알고리즘, n이 10^6이니.. nlog미만 
    count = 0
    
    for i in range(len(split)):
        if prime_number(int(split[i])) == True :
            count+=1
    return count
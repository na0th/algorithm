def solution(numbers):
    import itertools
#   소수 체크 
    def is_prime_number(x):
        if x < 2 :
            return False
        for i in range(2,x) :
            if x % i == 0 :
                return False
        return True
    
    # nPr = itertools.permutations(arr, 2)
    number_list = list(numbers)
    
    answer = []

    for i in range(1,len(numbers)+1) :
        answer += set(list(itertools.permutations(numbers,i)))
      
        

    cnt = 0    
    result = []
    for item in answer :
        result.append(int(''.join(item)))
    result = set(result)

    for item in result :
        if is_prime_number(item) :
            cnt += 1

    
    return cnt
    
    
    
    
    
    
    
    
    
    
    
# #     모든 숫자를 만들어버린다.
# #   [1,7]이면 1,7,17,71이 가능함
# #   [0,1,1]이면 0, 1 , 10, 11, 101, 110 (O)   011 001 (X)

#     import itertools
    
#     check_num = []
#     for i in range(len(numbers)):
#         check_num.extend(list(set(map(''.join, itertools.permutations(numbers,i+1)))))
#     print(check_num)
    
# #     그리고 맨앞에 0이 붙으면 0을 없애는 과정이 필요하다
# #     lstrip 사용하기
#     for i in range(len(check_num)):
#         check_num[i] = check_num[i].lstrip('0')
#         if check_num[i] == '' :
#             check_num[i] = '0'
    
#     check_num = list(set(check_num))
#     check_num.sort()
#     print(check_num)
#     print(len(check_num))
    
# #   소수 체크
#     count = 0
#     for num in check_num :
#         check = 0
#         for i in range(2,int(num)):
#             if int(num) % i == 0 :
#                 check=1
#                 break
#         if check == 0:
#             if int(num) >= 2 :
#                 count+=1
            
           

            
            
    
#     answer = count
#     return answer
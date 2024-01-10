def solution(number, k):
#     n이 10^6  = 1,000,000
#     n^2은 안되고, nlog ? or n 이하..

#  제일 먼저드는 생각은 콤비네이션 조합으로 완전탐색..
#  최악의 경우 10^6 C 5*10^5?? 이건 아닌 것 같다..

# 1924가 K가 1이면 924 , 2이면 94, 3이면 9.. 어떤 규칙일까?
# 1번씩 훑어서 924,94,9가 되는 게 아니고 순회하면서 한번에 다 줄여나가야
# 시간복잡도가 O(N)이 나올 수 있다..?

# 가면서 나보다 뒤에 숫자가 크면 나는 삭제..
# 그렇게한후 처음부터 다시 돈다.
#  BASE 포인트는 cnt가 K가 되면 끝!

# 시간초과가 나서 억지로 줄인 느낌이 있다...
    # number_list = list(number)
    
    cnt = 0
    i = 0
    while (cnt < k) :
        # if i == len(number_list)-1 :
        #     number_list = number_list[:cnt-k]
        if i == len(number)-1:
            number = number[:cnt-k]
            cnt += k
            break
        # if int(number_list[i]) < int(number_list[i+1]):
        #     del number_list[i]
        if number[i] < number[i+1] :
            number = number[:i]+number[i+1:]
            cnt += 1
            if i != 0 : 
                i -=1
                continue
            else :
                i = 0 
                continue
        i += 1
        
        
    return number 

    # answer = ''.join(number_list)    
    # return answer


    
    
    
    
    
    
    
    
    
    
    
#   맨 처음부터 내가 뒤 숫자보다 작으면 삭제 
#   삭제한 후에는 처음부터 다시 돈다
#   k개 삭제하면 break 
    
#     cursor = 0
#     while cursor < len(number)-1 and k > 0:
        
#         if number[cursor] < number[cursor+1]:
#             number =  number[:cursor] + number[cursor+1:]
#             k-=1
#             if cursor > 0 :
#                 cursor-=2
#             else :
#                 cursor-=1
        
#         cursor+=1
        
        
#     if k > 0  :
#         return number[:len(number)-k]
            
#     return number
    
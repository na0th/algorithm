
def solution(numbers):
    
#    34 , 331 , 3 , 30 , 31 이면 어떻게 해야 하나...
#    4자리까지 순환시켜서 만든다. 어차피 숫자는 1000이하니까!
#    3434 3313 3333 3030 3131
    


#   str(x)*4로 4자리까지는 순환되게 만든다. 어차피 1000이하라 괜찮다
    numbers.sort(key = lambda x:(str(x)*4), reverse=True)
    
    
#   11번 테스트 케이스 0,0,0,0 일 때는 0000이 아니라 0을 리턴해줘야 함    
#   이미 정렬은 된 상태이니 처음이 0이면 그냥 0 리턴
    if numbers[0] == 0 :
        return '0'
    answer = ''.join(list(map(str,numbers)))
    return answer
def solution(numbers):
    '''
    n보다 크면서 n하고 비트가 다른 지점이 1,2개 중 가장 작은 수?
    
    비트마스킹..
    비트는 십진수를 이진수로 변환한 값에 해당합니다.

    x가 짝수일 때
    2 -> 10 -> 11(3)
    4 -> 100 -> 101(5)
    6 -> 110 -> 111(7)
    짝수일 때는 그냥 +1 한 것..
    x가 홀수일 때
    1 -> 01 -> 10(2)
    3 -> 011 -> 101(5)
    5 -> 101 -> 110(6)
    7 -> 0111 -> 1011(11)
    홀수 일 때는 0나오면 나를 1 뒤에를 0
    1이나 7처럼 예외 있음.. 
    '''
#     answer = []
#     def trans_two(number):
#         num_list = []
#         while(number>0) :
#             q = number // 2
#             m = number % 2
#             number = q 
#             num_list.append(m)
#         num_list = list(map(str,num_list))
#         return num_list
    
#     for number in numbers :
#         answer.append(trans_two(number))
    
#     for number in answer :
#         if number[0] == '0' :
#             number[0] = '1'
#         else :
# #           0이 없다?
# #           => 맨앞에서 2번째에 0만 추가
#             if number.count(0) == 0 :
#                 number.insert(1,'0')
# #           맨처음부터 0 => 
#             for i in range(len(number)):
#                 if number[i] == '0' :
#                     number[i-1] = '0'
#                     number[i] = '1'
#                 break
                        
#     for i in range(len(answer)):
#         answer[i] = int(''.join(map(str, answer[i])),2)
#     return answer


    answer = []
    for i in numbers:
        num = i
        cnt = 0
        while (i % 2 == 1):
            cnt += 1
            i //= 2
        answer.append(num + 2**(cnt - 1) if cnt != 0 else num + 1)

    return answer
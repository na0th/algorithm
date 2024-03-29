def solution(n, left, right):
    
#   left부터 right까지 n개씩 묶어서 count가 묶음 개수보다 크면..
#   ex))  1,2,3,4 / 2,2,3,4 / 3,3,3,4 / 4,4,4,4 
#   1번 묶음   인덱스가 0이고 1이 1개, 나머지는 순차적으로 나머지+1
#   2번 묶음   인덱스가 1이고 2가 2개, 나머지는 순차적으로 나머지+1
#   3번 묶음   인덱스가 2이고 3이 3개, 나머지는 순차적으로 나머지+1
#   n번 묶음   인덱스가 n-1이고, n이 n개, 나머지는 순차적으로 나머지+1
    
    answer = []
    for i in range(left,right+1):
        div = i // n
        mod = i %  n
        if mod >= div :
            answer.append(mod+1)
        else :
            answer.append(div+1)
    return answer
    
    
    
    
    
    
    
    
    
#  ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ    
#   N*N 배열을 만들고, 재귀를 통해서 1은 00, 2는 01,11,01(2보다 다 작음)
#   3은 02,12,20,21,22(XY둘다 3보다 작으면서 1,2에서 안 채워진걸 채운다)

#  근데 위의 방식은 N이 10^7까지일 때 너무 터무니없다 
#              PASS



#  규칙 K번째 줄은 K를 K번 채우고 그뒤부터는 순차대로 N까지 채운다

#  예시 첫 번째줄은 1을 1번 채우고 그뒤부터는 2,3,4,5,6(크기 N)까지 적고
#      두 번째줄은 2를 2번 채우고 그뒤부터는 순차적으로 3,4,5,6 
#      세 번째줄은 3을 3번 채우고 그뒤부터는 4,5,6
    
#     left_line = (left // n) +1
#     right_line = (right // n) +1
    
#     list1 = [[0 for i in range(n)] for p in range(right_line)]

#     # for i in range(1,n+1):
#     #     for k in range(i):
#     #         list1[i-1][k]=i
#     #     for p in range(i,n):
#     #         list1[i-1][p]=p+1
            
# #   left_line 줄 추가
#     for i in range(left%n,n):
#         print(i)

# #   right_line 줄 추가
#     for i in range((right%n)+1):
#         print(i)
        
            
#     for i in range(left_line+1,right_line):
#         for k in range(i):
#             list1[i-1][k]=i
#         for p in range(i,n):
#             list1[i-1][p]=p+1
           
#     print(list1)
#     answer = []
    
#     for q in range(left,right+1):
#         q1 = q//n
#         q2 = q%n
#         answer.append(list1[q1][q2])
#     print(answer)
#     return answer
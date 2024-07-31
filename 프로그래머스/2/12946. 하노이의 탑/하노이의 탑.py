def solution(n):
    '''
    전체에서 맨 아래 원판이 A면 나머진 A'
    A'을 2번에 맨 아래 원판 A를 3번에 옮겨놓고 
    2번에 있는 걸 또 B'과 B로 구분해서 
    
    B'을 1번에 옮겨놓고 다시 B를 3번에 놓는다.
    
    계속 똑같은 게 반복된다..
    '''
    answer=[]
    def hanoi(left, mid, right, n) :
        if n ==  1:
            answer.append([left,right])
        else :
            hanoi(left, right, mid, n-1)
            answer.append([left,right])
            hanoi(mid, left, right, n-1)
    hanoi(1, 2, 3, n)
    return answer
    answer = []
 

#     def hanoi(left, mid, right, n):
#         if n == 1:
#             answer.append([left, right])
#         else:
#             hanoi(left, right, mid, n-1) 
#             answer.append([left, right])  
#             hanoi(mid, left, right, n-1) 

#     n = 3
#     hanoi(1, 2, 3, n)
#     print(answer)
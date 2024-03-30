def solution(n, t, m, p):
#   N은 N진법
#   T는 내가 말해야 하는 숫자 개수
#   M은 게임 참가 인원
#   P는 나의 순서
    
#   ex)) 10개 말할 것 5진법에 3명이라면 ? 난 2등

#   1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
#   1 2 3 4 10 11 12 13 14 15 20 21 22 23 24 25 
#   n진법으로 변환한 숫자를 그냥 전부 담는다.. 
#    m*n을 n진법으로 변환시켜 리스트에 담을 것이고, 그걸 p번째마다 뽑기

    def n_trans(n,q):
        string = ''
        while n > 0:
            n, mod = divmod(n, q)
            if mod == 10:
                mod = 'A'
            elif mod == 11:
                mod ='B'
            elif mod == 12:
                mod ='C'
            elif mod == 13 :
                mod ='D'
            elif mod == 14 :
                mod ='E'
            elif mod == 15 :
                mod = 'F'
            string += str(mod)

        return string[::-1] 
    
    
    list = ['0']
    for i in range(0,t*m+1):
        list.append(n_trans(i,n))
    
    list = ''.join(list)
    # print(list)
    
    answer = []
    for i in range(t):
        answer.append(list[p+(i*m)-1])
    
    return ''.join(answer)
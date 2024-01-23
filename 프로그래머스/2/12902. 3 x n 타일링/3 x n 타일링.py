def solution(n):
    dic = {2:3,4:11}
#   질문하기에서 테스트 케이스 보고 푼 문제(난이도가 훨씬 쉬워짐)
#   f(n)=3f(n-2)+2f(n-4)..까지는 나왔으나
#   간과한 게 lㅡㅡㅡㅡl  이런 모양을 옆에 추가해서 짝수마다 계속 생긴다는 걸 파악못함
#            ㅡㅡㅡㅡㅡ
#    여기서 맨 아래 들어간 가로벽 ㅡ의 위치를 맨위로 바꿔주는 경우의수 2가지씩을 곱하면
#  f(n) = 3f(n-2)+2f(n-4)+2f(n-6)+.....2

    for i in range(3,n+1):
        if i % 2 == 1 :
            dic[i] = 0
        else :
            if i-2 in dic and i-4 in dic :
                dic[i] = (4*dic[i-2]-dic[i-4])%1000000007
        
    answer = dic[n]%1000000007
    return answer

print(solution(6))


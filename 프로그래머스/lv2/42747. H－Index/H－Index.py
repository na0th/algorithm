def solution(citations):
#   정렬을 해보자
#     0,1,3,3,3,5,6     7편중 h번 이상 인용된 논문
#    0번 이상 인용된 논문 7개 나머지는 0번 이하 맞음
#    1번이상 인용된 논문 6개  나머지는 1번 이하 맞음
#    3번 이상 인용된 논문 5 (3번이상)  나머지는 3번 이하
#    그럼 return 3이다!
#    4번 이상 인용된 논문 2 (4번 이상X)  (나머지 4번 이하 X)
#    5번 이상 인용된 논문 2
#    6번 이상 인용된 논문 1
#     0,1,3,3,3,3,5,6
#  i.....len(citations)-1
#  i .... 4
#  i부터 끝까지 
#  0부터 i까지 개수 = h번 이하
#  0 1 .... i
    citations.sort()
    print(citations)
    for i in range(len(citations)):
        if citations[i]  >= len(citations)-i :
            return len(citations)-i
        if citations[-1] == 0 :
            return 0
      
    
    
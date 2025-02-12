def solution(k, d):
    '''
    요구사항 분석
    -> 원점과의 거리 d가 주어졌고, 배수(k)가 주어지면
    
    어떤 알고리즘 
    :수학? 원?
    
    어떻게 구현
    y = 0, d^2 = x^2 + y^2  -> d^2 = x^2
    y = 1, d^2 = x^2 -1 .. x는 0부터 시작, x는 루트(d^2-1)중 최대의 정수
    ...
    y는 0부터 d보다 작거나 같은 최대의 정수 까지 
    '''
    cnt = 0
    for y in range(0,d+1,k):
        x = (d**2 - y**2) **(1/2)
        cnt+=(x//k)+1
        # print("1",x)
        # print("2",x//k)
    
    return cnt
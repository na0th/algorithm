def solution(r1, r2):
    import math
    
    '''
    요구사항 정리 : 원 안에 있는 정수 쌍의 개수를 세는 코드를 찾자..
    
    알고리즘 분류 : 수학
    
    풀이 방법 : 
    total = 0 
    반원에 대해서 y가 0일 때의 y축을 제외한( x = 0) 정수 쌍 개수  *2 + 반지름(y축에 포함된 정수 쌍)
    위의 결과에 대해 * 2 => 원의 정수 쌍 개수
    
    
    
    '''

    
    def circle_cnt1(r):
        total = 0
        y = r
        for x in range(1,r) :
            while (x**2+y**2)>=r**2 :
                y=y-1
            total+=y
        return total*4
    def circle_cnt2(r):
        total = 0
        y = r
        for x in range(1,r) :
            while (x**2+y**2)>r**2 :
                y=y-1
            total+=y
        return total*4
            
                
    return circle_cnt2(r2)-circle_cnt1(r1)+4*(r2-r1)+4
    

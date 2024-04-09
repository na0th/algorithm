def solution(A,B):
    answer = 0
#   a<b , c<d 
#   [a,b] 와 [c,d]라면 ac+bd 와 ad+bc중의 부등호를 정해야 하는데
#   양변을 적절히 옮기면 a(d-c)<b(d-c)이므로 A에서 제일 큰 게 , B에서 제일 작은 것 뽑아서 곱하면 최소가 됨.
#  그래서 A정렬,B는 역정렬시키고 더하면 최소값 나올 것 같다. 
    A.sort()
    B.sort(reverse=True)
    
    for i in range(len(A)):
        
        num1 = A.pop(0)
        num2 = B.pop(0)
    
        answer+=num1*num2

    return answer
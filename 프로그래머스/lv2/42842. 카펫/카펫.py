def solution(brown, yellow):
    
    
    for a in range(1,2000000):
        for b in range(1,5000):
            if (a*b) == (brown + yellow) and 2*(a+b) == (brown+4) :
                if a>=b :
                    return [a,b]
                else : 
                    return [b,a]
                
            if (a+b>=brown*yellow) :
                break
                
#     x + y = 0.5 * (brown + 4)
#     x * y = brown + yellow
    answer = [1]
    return answer
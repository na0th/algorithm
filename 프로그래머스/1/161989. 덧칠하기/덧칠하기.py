def solution(n, m, section):
    
    section.sort(reverse=True)
    cnt = 0
    
    while(section):
        num = section.pop()
        while(section and section[-1] < num+m):
            section.pop()
        cnt+=1
        
    return cnt
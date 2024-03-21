def solution(order):
    cnt,stack,cursor = 0,[],0
    
    for i in range(1,len(order)+1):
        stack.append(i)
        while stack and stack[-1] == order[cursor] :
            stack.pop()
            cursor+=1
            cnt+=1
       

    return cnt
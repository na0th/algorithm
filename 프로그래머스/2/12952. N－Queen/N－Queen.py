def solution(n):
   
    '''
    백트래킹 문제..
    퀸 리스트가 있을 때,
    충돌이 나는지 안 나는지 체크하는 함수가 필요하다.
    
    element를 넣고 나서 백트래킹 해보고, 뺀 다음 넘어가
    이걸 0,0 (n-1,n-1) 까지..?
    
    
    current_set을 공유해도 되나? 
    
    '''
    def is_safe(queens, new_queen):
        
        new_row, new_col = new_queen

        for row, col in queens:
            if row == new_row or col == new_col: 
                return False

            if abs(row - new_row) == abs(col - new_col):  
                return False

        return True
    
    def backtrack(depth) :
        nonlocal cnt
        # base case ? depth로 지정해보자.. 
        
        if depth == n :
            cnt+=1
            return
    
        for col in range(n) :
            if is_safe(current_set,(depth,col)) :
                current_set.add((depth,col))
                backtrack(depth+1)
                current_set.remove((depth,col))
                
        return cnt
    
    current_set = set()
    cnt = 0
    return backtrack(0)
            
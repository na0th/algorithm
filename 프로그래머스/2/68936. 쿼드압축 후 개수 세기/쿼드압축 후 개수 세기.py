def solution(arr):
    '''
    4개로 나눌 수 있다.
    
    다 0이거나, 다 1이 아닌 경우는 4개로 나눔
    나눈 다음 각 각 다 0이거나 다 1이 아닌 경우는 4개로 나눠..
    다 0이거나 다 1이면? -> 0에 1더함, 1에 1더함으로 끝..
    
    4개로 나눠나눠 하다가 n이 1이 되면 숫자 세?
    '''
    
    def recursion(start_x,start_y,n):
        global cnt_zero, cnt_one
        if n == 1:
            if arr[start_x][start_y] == 1:
                cnt_one+=1
            else :
                cnt_zero+=1
            return
            #나를 더해야 하는데.. 내가 0이면 0 더하기, 1이면 1 더하기
        
        check = arr[start_x][start_y]

        for i in range(start_x,start_x+n):
            for j in range(start_y,start_y+n):
                if arr[i][j] != check:
                    recursion(start_x, start_y, n//2)
                    recursion(start_x, start_y + n//2, n//2)
                    recursion(start_x + n//2, start_y, n//2)
                    recursion(start_x + n//2, start_y + n//2, n//2)
                    return
                
        if check == 1:
            cnt_one += 1
        else:
            cnt_zero += 1
        
    global cnt_zero, cnt_one
    cnt_zero, cnt_one = 0, 0
    
    recursion(0,0,len(arr))
    return [cnt_zero,cnt_one]
def solution(board):
    '''
    구현
    전처리하여 문자열 -> 2차원 배열로 만들기
    
    for i in range(len(board)):
        board[i] = list(board[i])
    print(board)
    예외 상황만 처리
    
    개수가 안 맞는 경우
        1.X가 원래보다 적거나 많은 경우
        2.O가 원래보다 적거나 많은 경우
    X의 개수는 1턴:0, 2턴:1 , 3턴:1  4턴:2
    X의 개수는 N턴일 때 N을 2로나눈 몫이 된다.. -> N//2 
    
    O의 개수는 1턴:1, 2턴:1 , 3턴:2, 4턴:2, 5턴:3
    O의 개수는 N텉일때 N+1을 2로 나눈 몫.. -> (N+1)//2
    
    틱택토 완성품이 둘 다 1개 이상
    def ox_count(board) :
        o_count, x_count = 0, 0
        for i in range(3):
            if board[i][0] == board[i][1] and board[i][1] == board[i][2] :
                if board[i][0] == 'O' :
                    o_count +=1
                else :
                    x_count +=1

        for j in range(3):
            if board[0][j] == board[0][j] and board[0][j] == board[0][j] :
                if board[0][j] == 'O' :
                    o_count+=1
                else :
                    x_count+=1

        if board[0][0] == board[1][1] and board[1][1] == board[2][2] :
            if board[0][0] == 'O' :
                o_count+=1
            else :
                x_count+=1

        if board[0][2] == board[1][1] and board[1][1] == board[2][0] :
            if board[0][2] == 'O' :
                o_count+=1
            else :
                x_count+=1
    
    
    

    '''
    for i in range(len(board)):
        board[i] = list(board[i])
        
        
    def ox_count(board) :
        cnt_exp = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] != '.':
                    cnt_exp+=1
        if cnt_exp == 0 : 
            return 1
        o_count, x_count = 0, 0
        for i in range(3):
            if board[i][0] == board[i][1] and board[i][1] == board[i][2] :
                if board[i][0] == 'O' :
                    o_count +=1
                elif board[i][0] == 'X' :
                    x_count +=1

        for j in range(3):
            if board[0][j] == board[1][j] and board[1][j] == board[2][j] :
                if board[0][j] == 'O' :
                    o_count+=1
                elif board[i][0] == 'X' :
                    x_count +=1

        if board[0][0] == board[1][1] and board[1][1] == board[2][2] :
            if board[1][1] == 'O' :
                o_count+=1
            elif board[1][1] == 'X' :
                x_count +=1

        if board[0][2] == board[1][1] and board[1][1] == board[2][0] :
            if board[1][1] == 'O' :
                o_count+=1
            elif board[1][1] == 'X' :
                x_count +=1
        
        if (o_count >= 1 and x_count >= 1) :
            return 0
#       승자가 O라면
        if o_count >= 1:
#           둘의 차이가 1
            cnt_o, cnt_x = 0, 0
            for i in range(3):
                for j in range(3):
                    if board[i][j] == 'O' :
                        cnt_o +=1
                    elif board[i][j] == 'X' :
                        cnt_x +=1
            if cnt_o - cnt_x != 1:
                return 0
                
#       승자가 X라면 둘의 차이가 0
        elif x_count >= 1:
            cnt_o, cnt_x = 0, 0
            for i in range(3):
                for j in range(3):
                    if board[i][j] == 'O' :
                        cnt_o +=1
                    elif board[i][j] == 'X' :
                        cnt_x +=1
            if cnt_o - cnt_x != 0 :
                return 0
        return 1
        
    
    def right_count(board,word,n) :
        cnt = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == word :
                    cnt +=1
        if word == 'O' :
            if cnt == (n+1) // 2 :
                return 1
            else :
                return 0
        elif word == 'X' :
            if cnt == n // 2 :
                return 1
            else :
                return 0
    
    n = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != '.' :
                n+=1
    print(n,board)
    # answer = ox_count(board)
    print("ox_count=",ox_count(board),"rightO",right_count(board,'O',n),"rightX",right_count(board,'X',n))
    answer = ox_count(board) * right_count(board,'O',n) * right_count(board,'X',n)
    # answer = []
    return answer
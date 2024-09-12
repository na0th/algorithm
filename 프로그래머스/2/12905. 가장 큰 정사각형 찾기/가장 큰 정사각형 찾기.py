def solution(board):
    '''
    row와 column의 크기가 1000이하면
    1부터 1000까지 해보면 될 거 같은데는 안된다.
    1000*1000번
    + 999*999번
    +998*998번
    
    O(N^3)라서..
    
    1 1
    1 나 이라 치면
    ㅇ ㅇ ㅇ
    ㅇ ㅇ ㅇ
    ㅇ ㅇ X    X 부분만 커버가 안되는데, (내)가 1이면 커버가 되므로 연결이 된다.
    
    그래서 내가 1일 때, 왼쪽위, 내 위, 내 왼쪽중 최소의 값에서 +1 연결이 된다. 
    
    식으로는 dp[i][j] = min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j]) + 1 
    
    범위가 벗어나거나 하는 예외처리는 ? 만약 내가 0이라면?
    i or j =0 인 경우는 내가 0이면 0 1이면 1로 세팅해놓고  시작하면 될 것 같다.
    
    '''
    dp = [[0 for i in range(len(board[0]))] for j in range(len(board))]
#   i or j = 0 인 경우는 board[i][j]의 값이 '나'로 세팅
    for i in range(len(board)):
        for j in range(len(board[0])) :
            if i == 0 or j == 0 :
                if board[i][j]== 1 :
                    dp[i][j]=1
    # print(dp)
    
    
    for i in range(1,len(board)):
        for j in range(1,len(board[0])) :
            if board[i][j] == 1:
                dp[i][j] = min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])+1
    max_value = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if max_value< dp[i][j] :
                max_value = dp[i][j]
    # print(max_value)
    # print(dp)
    
    return max_value**2
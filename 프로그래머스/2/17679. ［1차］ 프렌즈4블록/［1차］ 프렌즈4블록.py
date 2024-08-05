def solution(m, n, board):
    board = [list(row) for row in board]
    
    def delete_four():
        cnt = 0
        bomb_list = set()
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != '0' and board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                    bomb_list.add((i, j))
                    bomb_list.add((i, j+1))
                    bomb_list.add((i+1, j))
                    bomb_list.add((i+1, j+1))
        if not bomb_list:
            return 0
        for item in bomb_list:
            x, y = item
            board[x][y] = '0'
        return len(bomb_list)
    
    def down():
        for j in range(n):
            column = [board[i][j] for i in range(m) if board[i][j] != '0']
            column = ['0'] * (m - len(column)) + column
            for i in range(m):
                board[i][j] = column[i]
    
    total_count = 0
    while True:
        count = delete_four()
        if count == 0:
            break
        total_count += count
        down()
    
    return total_count
    
    
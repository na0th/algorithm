def solution(board):
    
# 1칸씩 늘려서 인덱스 에러 안나게 한 후, 세어보자..
#     5*5면 7*7만들고  2~6까지만 세보자..

    
    n = len(board[0])
    
    mine = [[0]*(n+2) for _ in range(n+2)]
    mine2 = [[0]*(n+2) for _ in range(n+2)]
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            if board[i-1][j-1] == 1 :
                print(i,j)
                mine[i][j] = 1
                
    # print(mine)
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            if mine[i][j] == 1 :
                mine2[i-1][j-1]=1
                mine2[i-1][j]=1
                mine2[i-1][j+1]=1
                
                mine2[i][j-1]=1
                mine2[i][j]=1
                mine2[i][j+1]=1
                
                mine2[i+1][j-1]=1
                mine2[i+1][j]=1
                mine2[i+1][j+1]=1
                
    answer = 0
    print(mine)
    for i in range(1,n+1):
        for j in range(1,n+1):
            if mine2[i][j] == 0:
                answer+=1
    return answer  
    
    
    
    
    
    
    
    
    
    
#     import copy
#     mine = copy.deepcopy(board)
#     n = len(board[0])

#     for i in range(n):
#         for j in range(n):
#             if mine[i][j] == 1 :
#                 if j == 0 :
#                     if i == 0 :
#                         mine[i][j+1] = 1
#                         mine[i+1][j] = 1
#                         mine[i+1][j+1] = 1
#                         continue

#                     if i == n-1 :
#                         mine[i-1][j] = 1
#                         mine[i-1][j+1] = 1
#                         mine[i][j+1] = 1
#                         continue

#                     mine[i-1][j]=1
#                     mine[i-1][j+1]=1
#                     mine[i][j]=1
#                     mine[i][j+1]=1
#                     mine[i+1][j]=1
#                     mine[i+1][j+1]=1
#                     continue

#                 if j == n-1 :
#                     if i == 0 :
#                         mine[i][j-1]=1
#                         mine[i+1][j-1]=1
#                         mine[i+1][j]=1
#                         continue
#                     if i == n-1 :
#                         mine[i-1][j-1]=1
#                         mine[i-1][j]=1
#                         mine[i][j-1]=1
#                         continue
#                     mine[i-1][j-1]=1
#                     mine[i-1][j]=1
#                     mine[i][j-1]=1
#                     mine[i][j]=1
#                     mine[i+1][j-1]=1
#                     mine[i+1][j]=1
#                     continue


#                 mine[i-1][j-1]=1
#                 mine[i-1][j]=1
#                 mine[i-1][j+1]=1

#                 mine[i][j-1]=1
#                 mine[i][j]=1
#                 mine[i][j+1]=1

#                 mine[i+1][j-1]=1
#                 mine[i+1][j]=1
#                 mine[i+1][j+1]=1
    
#     print(mine)
            
#     answer = 0
#     return answer
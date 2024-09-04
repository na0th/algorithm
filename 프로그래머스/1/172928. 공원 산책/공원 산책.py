def solution(park, routes):
    '''
    1. 이동하려다 공원을 벗어나면 이동안 할 것
    2. 이동하려다 장애물을 만난다면 이동하지 않을 것
    '''
    
    point = []
    x,y = 0,0
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S" :
                x = i
                y = j
    # print(x,y)
    # s_list = ["SOO", "OXX", "OOO"]
    # print(s_list[1][0:3])
    for item in routes: 
        s_list = item.split(" ")
        # print(s_list)
        point.append(s_list)

    # print(point)
    for itm in point:
        nx, ny = 0,0
        if itm[0] == 'W' :
            ny = y - int(itm[1])
        elif itm[0] == 'E':
            ny = y + int(itm[1])
        elif itm[0] == 'N' :
            nx = x - int(itm[1])
        elif itm[0] == 'S' :
            nx = x + int(itm[1])  
        # print("nx,ny",nx,ny)
#           이동 후에 벗어나는지 check
        if  0 <= nx < len(park) and 0<= ny < len(park[0]) :
            
#           도중에 장애물을 만나는지 check
            if itm[0] == 'W' :
                # print(park[x][min(y, ny):max(y, ny) + 1])
                # if 'X' not in park[x][min(y, ny):max(y, ny) + 1]:
                if 'X' not in park[x][min(ny, y):max(ny, y) + 1]:  
                    y = ny  
            elif itm[0] == 'E':
                # print(park[x][min(y, ny):max(y, ny) + 1])
                if 'X' not in park[x][min(y, ny):max(y, ny) + 1]:
                    y = ny
            elif itm[0] == 'N' :
                # print(park[min(x, nx):max(x, nx) + 1][y])
                # if 'X' not in park[min(x, nx):max(x, nx) + 1][y] :
                if 'X' not in [park[i][y] for i in range(min(nx, x), max(nx, x) + 1)]:
                    x = nx
            elif itm[0] == 'S' :
                # print(park[min(x, nx):max(x, nx) + 1][y])
                # if 'X' not in park[min(x, nx):max(x, nx) + 1][y] :
                if 'X' not in [park[i][y] for i in range(min(x, nx), max(x, nx) + 1)]:
                    x = nx

                    
    return [x,y]

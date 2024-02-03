def solution(dirs):
#   방문 리스트를 기억해놔야 겠다.
#   before - after로 방문했는데 순서는 상관 없으니 정렬한다.
#   좌표 벗어나면 이동하지 않는다.
    visited_list = []
    
    before=[0,0]
    
    for item in dirs:
        after = before.copy()
        if item == "L" :
            if after[0] <= -5:
                continue
            after[0]-=1
        elif item == "R" :
            if after[0] >= 5:
                continue
            after[0]+=1
        elif item == "U" :
            if after[1] >= 5:
                continue
            after[1]+=1
        elif item == "D" :
            if after[1] <= -5:
                continue
            after[1]-=1
        
        add = [before,after]
        add.sort()
        
        if add not in visited_list :
            visited_list.append(add)

        
        before = after
        # print(after)
        
    # print(visited_list)

    answer = len(visited_list)
    return answer
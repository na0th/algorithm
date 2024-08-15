def solution(land):
    '''
    같은 열을 연속해서 밟을 수 없다..
    그리디? x 
    dp? 몰라
    완전탐색 ? 몰라
    cur_max + next 3개중 하나  or cur_max 제외한 3개 중 max + next curmax열
    
    따라서 필요한 건 max랑 뭐 밟았는지만 필요하다
    
    [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
    5랑 5 다음 8을 제외한 max 7 vs 5를 제외한 max 3과 8 중 하나
    
    '''
    
    
    
    for j in range(1, len(land)):
        land[j][0] += max(land[j-1][1], land[j-1][2], land[j-1][3])
        land[j][1] += max(land[j-1][2], land[j-1][3], land[j-1][0])
        land[j][2] += max(land[j-1][3], land[j-1][0], land[j-1][1])
        land[j][3] += max(land[j-1][0], land[j-1][1], land[j-1][2])

    return max(land[-1])


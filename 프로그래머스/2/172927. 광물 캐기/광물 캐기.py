def solution(picks, minerals):
    from collections import Counter
    import heapq
    """
    다이아는 다이아 1 철 1 돌 1
    철 곡괭이는 다이아몬드를 캐려면 피로도 5, 철 1, 돌 1
    돌은 다이아몬드는 25 철 5 돌 1
    
    각 곡괭이는 종류에 상관없이 광물 5개를 캔 후에는 사용할 수 없다.
    최소한의 피로도로 광물을 캐려고 한다
    곡괭이중 아무거나 선택해 광물을 캐고 , 사용할 수 없을 때까지(5번)까지 캔다
    광물은 주어진 순서대로만 캐야한다.
    모든 광물을 캐거나, 곡괭이가 없을 때까지 캡니다.
    
    최소한의 피로도를 리턴하세요!
    
    최소의 피로도를.. 어떻게??
    1, 5, 25라 그리디가 되나?
    다이아가 있으면 무조건 다이아,돌, 철 순서대로 써야함
    다이아가 없고 철부터 있다면? 돌을 철보다 먼저 써야함..
    근데 철*5 + 다이아*5가 있어 곡괭이는 1,1,1이면 철 때는 다이아를 아끼는 게 좋은데
    
    
    
    
    
    5개씩 묶어서 value를 정하고 정렬한다 그리고 곡괭이 비싼 거 먼저 쓰면 될 거 같다.
    
    
    """
    maxMinerals = sum(picks) * 5
    
    # 광물 배열을 곡괭이의 수에 따라 잘라냄
    if len(minerals) > maxMinerals:
        minerals = minerals[:maxMinerals]
    value_list = []
    for i in range(0,len(minerals),5) :
        pick_five = minerals[i:i+5]
        # print(minerals[i:i+5])
        total = 0
        for j in range(len(pick_five)) :
            if pick_five[j] == 'diamond':
                total += 25
            elif pick_five[j] == 'iron' :
                total += 5
            elif pick_five[j] == 'stone' :
                total += 1
        value_list.append((total, pick_five.count('diamond'), pick_five.count('iron'), pick_five.count('stone')))
        
    value_list.sort(key=lambda x:x[0], reverse=True)
    
    
    # print(value_list)
    ex = 0      
    for total, diamond_count, iron_count, stone_count in value_list :
        if picks[0] >= 1:
            ex += diamond_count + iron_count + stone_count
            picks[0]-=1
        elif picks[1] >= 1 :
            ex += diamond_count * 5 + iron_count + stone_count
            picks[1]-=1
        elif picks[2] >= 1 :
            ex += diamond_count * 25 + iron_count * 5 + stone_count
            picks[2]-=1
        else :
            break        
    return ex
    

    
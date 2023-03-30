def solution(genres, plays):
    hash_table = {}
    for i in range(len(genres)):
        if genres[i] not in hash_table :
            hash_table[genres[i]] = [0,[]]
        hash_table[genres[i]][0]+=plays[i]
        hash_table[genres[i]][1].append([plays[i],i])
    
    new_table = sorted(hash_table.values(),key=lambda x:x[0],reverse=True)
#   이제 딕셔너리 필요 없습니다.
    # print(new_table)
    answer=[]
    for i in range(len(new_table)):
        new_table[i][1].sort(key=lambda x:x[0],reverse=True)
        if len(new_table[i][1]) == 1 :
            answer.append(new_table[i][1][0][1])
        else :
            answer.append(new_table[i][1][0][1])
            answer.append(new_table[i][1][1][1])
    print(new_table)
    
    # list1 = [[600, 1], [2500, 4]]
    # list1.sort(key=lambda x:x[0], reverse=True)
    # print(list1)
    
    
    return answer
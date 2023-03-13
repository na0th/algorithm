def solution(k, dungeons):
    import itertools 
#   인덱스 배열
    arr = [_ for _ in range(len(dungeons))]
#   인덱스 배열을 순서쌍으로 만들기
    per_arr = list(set(itertools.permutations(arr,len(dungeons))))
    temp = k
#   인덱스 배열을 쭉 돌면서 최대 던전 수를 return하도록 한다
    list1=[]
    
    for sett in per_arr :
        k = temp
        count = 0
        for idx in sett :
            if k >= dungeons[idx][0] and k >= dungeons[idx][1]+1:
                k-=dungeons[idx][1]
                count+=1
                # if count > max_count :
                #     max_count = count
        list1.append(count)

   
            
                
#  그리고 최대 배열의 수가 이미 던전 수랑 같아지면 그냥 끝낸다.

        
    
    
    
    answer = max(list1)
    return answer
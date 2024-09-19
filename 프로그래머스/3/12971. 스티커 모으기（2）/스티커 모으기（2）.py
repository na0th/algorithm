def solution(sticker):
    '''
    원형으로 연결된 스티커, 스티커를 떼면 양쪽으로 인접해있는 스티커는 찢어진다.
    ex 14를 뜯으면 10과 6은 사용못함..
    어떻게 푸나 

    dp? 
    
    1 2 3 4 5 6 7 8 까지 있따하면
    
    dp[1] = 그냥 그 number
    dp[2] = 그냥 그 number인데
    dp[3] = 까지는 고정
    
    dp[4]부터는 2칸전에서 온 거랑, 3칸 전에서 온 거랑 max를 담아야 해
    
    1을 떼면서 시작하는 경우 vs 2를 떼면서 시작하는 경우로 나눠보자
    
    그렇게 안하면 최대를 구했더니 마지막 7,8번이 붙어있는 경우가 나옴..
    
    '''
    if len(sticker) == 3 :
        return max(sticker[0]+sticker[2],sticker[1])
    if len(sticker) == 2:
        return max(sticker[0],sticker[1])
    if len(sticker) == 1:
        return sticker[0]

    dp1 = {0:sticker[0],1:sticker[1],2:sticker[0]+sticker[2]}
    dp2 = {1:sticker[1],2:sticker[2],3:sticker[1]+sticker[3]}
    
    # print(dp1)
    # print(dp2)
    #1234567
    for i in range(3,len(sticker)-1):
        dp1[i]=max(dp1[i-2],dp1[i-3])+sticker[i]
    
    #2345678
    for j in range(4,len(sticker)):
        dp2[j]=max(dp2[j-2],dp2[j-3])+sticker[j]
        
  
    return max(max(dp1.values()),max(dp2.values()))

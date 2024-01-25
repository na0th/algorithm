def solution(common):
    
    # // 등차수열일 때
    if abs(common[2]-common[1]) == abs(common[1]-common[0]):
        return common[0]+(common[1]-common[0])*(len(common))
    # // 등비수열일 떄
    else : 
        return common[0]*(common[1]/common[0])**(len(common))
   
    answer = 0
    return answer
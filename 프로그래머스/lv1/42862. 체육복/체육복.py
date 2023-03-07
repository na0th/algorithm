def solution(n, lost, reserve):
#   일단 여벌이 있는 학생중 도난 당했는지 아닌지를 체크해야 함
#   먼저 도둑맞은 reserve 학생들은 둘 다 제거하고 시작
    lost.sort()
    reserve.sort()
    for i in range(len(reserve)):
        if reserve[i] in lost:
            lost.remove(reserve[i])
            reserve[i] = 100
            continue

    for i in range(len(reserve)) :
#    왼쪽부터 준다, 준다음은 continue로 넘어가게
        if reserve[i]-1 in lost :
            lost.remove(reserve[i]-1)
            reserve[i] = 100
            continue
            
        if reserve[i]+1 in lost :
            lost.remove(reserve[i]+1)
            reserve[i] = 100
            continue
            
        
    
    answer = n-len(lost)
    return answer
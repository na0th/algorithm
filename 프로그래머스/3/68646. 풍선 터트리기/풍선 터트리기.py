def solution(a):
    '''
    인접한 두 풍선 중에서 번호가 더 작은 풍선을 터트리는 행위는 최대 1번
    따라서 , 인접한 두 풍선을 골라 큰 거를 터트리는 걸로 하되, 최대 1번은 작은 걸 터트릴 것
    터진 풍선으로 인해 빈공간이 생기면 풍선을 중앙으로 밀착
    
    길이가 10^6? n^2은 절대 안됨.
    
    
    왼쪽에서 최소, 오른쪽에서 최소를 구해서 둘 다 나보다 작아? 그럼 걘 안돼
    
    왼쪽에서 최소 -> 나와 직전 최소만 비교하면 됨.
    '''

    min_until_left = [float("inf") for i in range(len(a))]
    min_until_right = [float("inf") for i in range(len(a))]
    for i in range(len(a)):
        if i == 0  :
            min_until_left[i] = a[i]
        else : 
            min_until_left[i] = min(min_until_left[i-1],a[i])
            
    for i in range(len(a)-1,-1,-1) :
        if i == len(a)-1 :
            min_until_right[i] = a[i]
        else :
            min_until_right[i] = min(min_until_right[i+1],a[i])

    
    # print(min_until_left)
    # print(min_until_right)
    
    cnt = 0
    for i in range(len(a)) :
        if a[i] <= max(min_until_left[i],min_until_right[i]) :
            cnt+=1
    return cnt
        
    
    

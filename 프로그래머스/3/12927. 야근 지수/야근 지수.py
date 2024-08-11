import heapq
def solution(n, works):
    '''
    야근 피로도가 쌓임
    야근을 시작한 시점에서 남은 일의 작업량을 제곱하여 더한 값
    n시간동안 야근 피로도를 최소화 하도록.. 1시간에 1 처리가능
    
    최대값을 뽑아서 계속 -1 해야 하므로 우선순위큐 MaxHeap 쓰기
    '''
    
    works = [i*-1 for i in works]
    
    heapq.heapify(works)
    for i in range(n) :
        pop = heapq.heappop(works)
        if pop != 0 :
            pop+=1
        heapq.heappush(works,pop)
    
    answer = sum(i**2 for i in works)

    return answer
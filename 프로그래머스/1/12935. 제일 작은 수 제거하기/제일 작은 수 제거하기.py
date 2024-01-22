def solution(arr):
    if len(arr) == 1 :
        return [-1]
    
    min1 = min(arr)
    
    arr.remove(min1)
    return arr
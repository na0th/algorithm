def solution(arr):
    answer = []
   
    for i in range(len(arr)):
        if arr[i] not in answer :
            answer.append(arr[i])
        else :
            if i > 0 :
                if arr[i-1] != arr[i]:
                    answer.append(arr[i])
            continue
    
    return answer
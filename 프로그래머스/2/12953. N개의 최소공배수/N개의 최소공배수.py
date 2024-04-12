def solution(arr):
#   크기 순으로 정렬하고..
    arr.sort(reverse=True)

#   [14,8,6,2]라면?
    
    memory = arr[0]
#    14를 8로 계속 나눈다.. 1--6 : 나머지가 0이므로 
    for i in range(len(arr)-1):
        a = memory
        b = arr[i+1]
        
        while (a%b != 0) :
            a,b = b, a % b
        memory = int((memory*arr[i+1])/b)

    # print(memory)
    answer = memory
    return answer
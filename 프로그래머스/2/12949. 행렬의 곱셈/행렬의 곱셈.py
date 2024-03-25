def solution(arr1, arr2):
#   행렬의 곱 배열은 n*p 와 p*q의 곱이라면 n*q가 된다..
    # len(arr1)은 행, len(arr1[0])은 열의 수를 가리킨다
    # print(len(arr1),len(arr1[0]))
    
#   행렬 곱하면 그냥 len(arr1) * len(arr2[0])의 행렬이 나오겠군!
#   왜냐, n * p 와 p * q 니까..

#  결과 행렬을 0으로 다 초기화시키기

    answer = [[0 for i in range(len(arr2[0]))] for j in range(len(arr1))]
    
#  행렬 곱한 걸 계속 더해서 리턴하자..
#  그전에 arr2를 전치행렬로 만들자..
    new_arr2 = []
    
    for i in range(len(arr2[0])):
        column = []
        for row in arr2:
            column.append(row[i])
        new_arr2.append(column)
        
    arr2 = new_arr2
    
#   arr1의 행, arr2의 열을 곱한다.. 그걸 [행-1][열-1]에 더한다..
    for row in range(len(arr1)):
        for col in range(len(arr2)):
            # print("row = ",arr1[row])
            print()
            # print("col = ",arr2[col])
            print()
            for k in range(len(arr2[0])): 
                # print(arr1[row][k],arr2[col][k])
                answer[row][col]+=arr1[row][k]*arr2[col][k]

    return answer

        
        
    



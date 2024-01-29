def solution(data, col, row_begin, row_end):
#   튜플 2500

#   col 기준으로 sort
#   같으면? 첫 번째 컬럼을 기준으로 정렬하되 내림차순..? -부호로 해결
    data = sorted(data,key=lambda x:(x[col-1] ,-x[0]))
    # print(data,1)
    
#   정렬 끝났으니 S_i를 정의하기
    answer_list=[0]
    for i in range(len(data)):
        total = 0
        for j in range(len(data[i])):
            total += (data[i][j] % (i+1))
        answer_list.append(total)
    
    # print(answer_list)
    
#   XOR 연산을 계속한다.
    add = answer_list[row_begin]
    for i in range(row_begin+1,row_end+1):
        add = (add) ^ (answer_list[i])
    return add
        
    # return (answer_list[row_begin])^(answer_list[row_end])

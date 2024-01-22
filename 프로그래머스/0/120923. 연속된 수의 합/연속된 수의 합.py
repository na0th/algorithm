def solution(num, total):

#    num , total  a~b 
#    홀 홀     중앙값 +- num -1 // 2  n n+1 n+2 / 3n+3  5n+10
#    3 15  // 4 5 6   -> 중앙이 total / num = 5
#    홀 짝
#    3  12  // 3 4 5   -> 중앙이 total / num = 4
#    짝 홀
#    2  7  // 3 4  --> 중앙 (3.5) 내리면 3 
#  만약 6 21였다면? 6  123 3.5 456

#    짝 짝
#    4  10  [1,2,3,4]
#    8  36   1234 4.5 5678
    middle_num = (total//num)
    if num % 2 == 1 :
        return [x for x in range(middle_num-((num//2)),middle_num+((num//2)+1))]
    else :
        return [x for x in range(middle_num-(num//2)+1,middle_num+num//2+1)]
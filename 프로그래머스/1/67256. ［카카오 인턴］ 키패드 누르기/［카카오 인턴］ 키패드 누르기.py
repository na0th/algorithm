def solution(numbers, hand):
#   왼손 위치 변수 '' , 오른손 위치 변수 ""
#  눌러야 할 손까지 거리를 구한다. 같으면 왼손,오른손잡이 손 따라서..

    dic = dict()
    dic['1']=[1,1]
    dic['2']=[1,2]
    dic['3']=[1,3]
    dic['4']=[2,1]
    dic['5']=[2,2]
    dic['6']=[2,3]
    dic['7']=[3,1]
    dic['8']=[3,2]
    dic['9']=[3,3]
    dic['*']=[4,1]
    dic['0']=[4,2]
    dic['#']=[4,3]
    
    now_left='*'
    now_right='#'
    answer = []
    for number in numbers:
        if number in [1,4,7] :
            answer.append("L")
            now_left = str(number)
            continue
        if number in [3,6,9] :
            answer.append("R")
            now_right = str(number)
            continue
        else :
            number = str(number)
            left_distance_x = abs(dic[now_left][0]-dic[number][0])
            left_distance_y = abs(dic[now_left][1]-dic[number][1])

            right_distance_x = abs(dic[now_right][0]-dic[number][0])
            right_distance_y = abs(dic[now_right][1]-dic[number][1])

            left_sum_distance = left_distance_x +left_distance_y
            right_sum_distance = right_distance_x+right_distance_y
        
            if left_sum_distance > right_sum_distance:
                answer.append("R")
                now_right = number
                continue
            if left_sum_distance < right_sum_distance:
                answer.append("L")
                now_left = number
                continue
            else :
                if hand == "right":
                    answer.append("R")
                    now_right = number
                else :
                    answer.append("L")
                    now_left = number

    answer = ''.join(answer)
    return answer
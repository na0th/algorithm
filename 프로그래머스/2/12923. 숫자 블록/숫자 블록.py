def solution(begin, end):
#   약수 몇개인지 구하라는 뜻 start부터 end까지 => 아니다.. 
#   문제 제대로 읽기 ~

# 기존에 설치된 블록은 빼고 새로운 블록을 집어넣습니다.
#  가장 큰 약수를 구하라..? => 맞았음

# 소수면 1.. 근데 10억까지면 완전탐색해서 소수 찾을 수 있겠군..
#  + 소수 구하는 방법이 가장 기본 방법 말고도 뭔가 있는 듯하다
#  루트(num)까지 해서 나눠진 게 없어도 소수라한다


# 짝수면 나누기 2 ,

# 홀수면 엑시던트지만, 그냥 제일 먼저 나눠지는 수로 나누면 된다 

#  홀수 짝수 나눌 필요가 없다 생각해보니 그냥 나눠지면 그걸로 하면된다

#  문제 제대로 읽기. 길이 1,000,000,000인 도로에
#  10,000,000까지 블록을 이용해 규칙대로 모두 설치했다..

# 
# 13번이랑 효율성이 오류난다..
    import math
    def return_answer(n):
        num_list = []
        for i in range (2, int(math.sqrt(n) + 1)):	
        # for i in range(2, n + 1):
            if n % i == 0:
                num_list.append(i)
                if n//i <= 10000000:
                    num_list.append(n//i)
        if not num_list :
            return 1
        else :
            return max(num_list)
        


            
    # print(prime_number(100000000003))
    
#  아래 예시로 감 잡았음
    # list1 = [0 for _ in range(30)]
    # for i in range(1,31) :
    #     for j in range(1,31) :
    #         if j % i == 0 and j > i :
    #             list1[j-1] = i
    # print(list1)
    answer = []
    for i in range(begin,end+1):
        if i == 1 :
            answer.append(0)
            continue
        number = return_answer(i)
        answer.append(number)
   
    return answer
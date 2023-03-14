def solution(people, limit):
#  방법 1)
#   일단 정렬을 시켜서 맨 앞 숫자와 다른 숫자들을 각각 더해본다
#   계속 limit 보다 작다가 어느 순간 limit보다 커지는 순간이 존재한다
#   ex )   10 30 50 60 70 80 90 95   limit 100 
#    여기서 10+30, 10+50, 10+60 ... 10+95 (X)
#    그럼 10,90을 삭제한다 2개 삭제하고 count+=1
#    그리고 30 50 60 70 80 95로 똑같이 반복
#    그럼 30,70을 삭제한다   2개 삭제하고 count+=1
#    그리고 50 60 80 95가 남는데 똑같이 반복하려는데!!
#    처음부터 바로 옆에를 더했을 때 limit를 넘어버린다 .
#    그러면 모두 2명이서 탈 수 없다는 뜻이므로 남은 숫자들을 count+1씩 해버린다
#  효율성이 안좋음

#  만약 people 첫값과 끝값이 limit를 애초에 넘지 않는다면?
#  홀수면 n/2+1 , 짝수면 n/2 리턴하면 된다..

#  다른 방법 2) 이게 더 좋아보임
#  정렬해서 맨 처음 맨 끝을 더해서 맨끝에서부터 안되면 포인터를 왼쪽으로 옮긴다
#  되는 놈이 나오면 그 때 그 둘을 삭제해버린다. count+=1
#  그리고 계속 돌린다..
#  계속 오른쪽 포인터를 왼쪽으로 옮기다 서로 같아지면 그때는 그만두고 
#  남은 숫자들을 각각 1개씩 count+1 해버린다
#  효율성이 안좋음

#  완벽하게 투포인터로 그냥 풀어보자

#   people 정렬
    people.sort()
    
    run = True
    boat_count = 0
    left = 0
    right = len(people)-1
  
    while(left < right) :
        if people[left] + people[right] > limit :
            right-=1
        elif people[left] +people[right] <= limit :
            left+=1
            right-=1
            boat_count+=1
            
    print(len(people)-boat_count)
    
            
    
    answer = len(people)-boat_count*2+boat_count
    return answer
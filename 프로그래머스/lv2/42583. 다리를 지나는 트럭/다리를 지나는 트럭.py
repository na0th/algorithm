def solution(bridge_length, weight, truck_weights):
#   대기 트럭에서 다리 건너는 트럭의 총 무게, 길이 조건에 맞으면 건너게 한다.
#   다리를 지나갔으면 다리를 지난 것으로 옮긴다.
#   다리를 건너는 트럭 , 대기 트럭이 비어있으면 종료

    going_truck = []
    time_truck = []
    time = 0
    
    
    while True:
        
        if len(time_truck) > 0 :
            check = -1
            for i in range(len(time_truck)):
                time_truck[i]-=1
                if time_truck[0] == 0 :
                    check = 1
            if check == 1 :   
                del going_truck[0]
                del time_truck[0]
                
                
#       뽑은 트럭이 올라가도 트럭 무게가 다리가 버틸 수 있어야 하고, 길이보다 트럭 수가 작아야한다.
        if sum(going_truck)+truck_weights[0] <= weight and len(going_truck)+1 <= bridge_length :
                pop = truck_weights.pop(0) 
                going_truck.append(pop)
                time_truck.append(bridge_length)
                
        
        time+=1
    #   종료 
        if  not truck_weights :
            return time+bridge_length
    
            
        
        
    
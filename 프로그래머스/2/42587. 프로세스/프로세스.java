import java.util.*;
class Solution {
    /*
    특정 프로세스가 몇번째로 실행되는지 알아내기
    1 실행 대기 큐에서 프로세스 하나 꺼내기
    2 우선순위 중 제일 높은지 확인해서 아니면 다시 대기 큐에 넣기
    3 제일 높은 프로세스면 프로세스 실행하기
    알고리즘 분류 : 큐
    어떻게 풀이?
    
    인덱스, 우선순위를 묶은 자료구조 만들기
    우선순위에 따라 프로세스 실행하거나, 대기 큐에 넣거나 함
    location에 있는 큐가 실행되면서 카운트를 출력
    */
    public int solution(int[] priorities, int location) {
        Deque<int[]> queue = new ArrayDeque<>();
        
        for(int i=0; i<priorities.length; i++){
            queue.addLast(new int[]{i,priorities[i]});
        }
        int count = 0;
        while(!queue.isEmpty()){
            int[] pop =queue.removeFirst();
            int idx = pop[0];
            int priority = pop[1];
            
            boolean isMax = queue.stream().anyMatch(p -> p[1] > priority);
            if(isMax){
                queue.addLast(pop);
            }else{
                count++;
                if(idx == location){
                    return count;
                }
            }

        }
        return -1;
    }
}
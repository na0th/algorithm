import java.util.*;
class Solution {
    /*
    섞은 스코빌 지수 = 가장 맵지 않은 스코빌 지수 + (두 번째로 맵지 않은 스코빌 지수 * 2)
    분류 : 힙 
    가장 작은 2개를 계속해서 꺼내야 함. 그리고 새로 만든 값이 추가되어야 함.
    
    어떻게 풀이?
    1. min 우선순위큐 사용해서 최소값을 2개 뽑는다. 
    2. 뽑은 2개가 전부 k를 넘으면 끝낸다.
    3. 그렇지 않으면, 둘을 더해서 다시 우선순위큐에 넣는다.
    
    예외처리
    모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return
    
    루프문에서 heap.peek이 K 이상일 때, answer를 더하지 않고 즉시 0을 리턴하는가
    heap의 size가 2보다 작아 루프에서 탈출했을 때, heap.peek이 K 이상인지 확인 후 answer를 return 하는가
    */
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        
        for(int s : scoville){
            pq.offer(s);
        }
        
        while(pq.size() >= 2){
            int num1 = pq.poll();
            int num2 = pq.poll();
            int mix = num1 + 2 * num2;
            
            if (num1>=K && num2>=K){
                return answer;
            }
            pq.offer(mix);
            answer+=1;
        }
        if (pq.poll()>=K){
            return answer;
        }
        return -1;
    }
}
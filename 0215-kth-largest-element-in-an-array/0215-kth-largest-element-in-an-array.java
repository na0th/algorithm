import java.util.*;

class Solution {
    /**
    k 번째로 큰 수(숫자들은 유니크하지 않다)
    알고리즘 분류 : 힙, 우선순위 큐 
    어떻게 풀이? 
    
    */
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        
        for(int num : nums){
            pq.add(num);
        }
        for(int i = 0; i<k-1; i++){
            pq.remove();
        }
        return pq.poll();
    }
}
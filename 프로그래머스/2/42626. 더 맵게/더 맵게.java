import java.util.*;
class Solution {
    public int solution(int[] scoville, int K) {
        int ans = 0;
        
        PriorityQueue<Integer> pq = new PriorityQueue<>();
            
        for (int s : scoville) {
            pq.add(s);            
        }

        while (!pq.isEmpty()) {
            int min = pq.remove();
            
            if (min >= K) {
                return ans;
            }
            
            if (!pq.isEmpty()) {
                int second = pq.remove();
                pq.add(min + (second * 2));
                ans++;
            } else {
                return -1;
            }
        }
        return ans;
    }
}
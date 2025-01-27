import java.util.*;
import java.io.*;
class Solution {
    public int solution(int[] scoville, int K) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        
        for(int num : scoville){
            pq.add(num);
        }
        
        int cnt = 0;
        
        while(pq.size() >= 2) {
            
            int min_num1 = pq.poll();
            if (min_num1 >= K) {
                return cnt;
            }
            int min_num2 = pq.poll();
            int mix_num = min_num1+min_num2*2;
            
            pq.add(mix_num);
            cnt+=1;
        }
        if (pq.poll()<K){
            return -1;
        }
        else{
            return cnt;
        }
        
    }
}
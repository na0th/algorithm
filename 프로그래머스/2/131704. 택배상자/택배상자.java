import java.util.*;
import java.io.*;
class Solution {
    /*
    1 2 3 ... n번의 상자가 존재
    왼쪽부터 내림.. 보조 컨테이너 벨트에 보관해야 함..(마지막에 보관한 상자부터 꺼냄)
    
    */
    public int solution(int[] order) {
        Deque<Integer> deque = new ArrayDeque<>();
        int cursor = 0;
        int cnt = 0;
        for(int i = 1; i<=order.length;i++){
            deque.addLast(i);
            while(!deque.isEmpty() && deque.getLast() == order[cursor]){
                deque.removeLast();
                cursor++;
                cnt++;
               
            }
            // System.out.println(order[i]);
        }
        
        return cnt;
    }
}
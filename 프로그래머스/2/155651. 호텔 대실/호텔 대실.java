import java.util.*;
import java.io.*;
class Solution {
    public int solution(String[][] book_time) {
        /*
        대실 이용 후에는 10분 후에 손님을 받을 수 있다.
        필요한 최소 객실의 수
        세로로 줄을 그었을 때, 최대 = 
        */
        
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        Arrays.sort(book_time, (a, b) -> convertToMinutes(a[0]) - convertToMinutes(b[0]));

        int maxRooms = 0;
        
        for(String[] slot : book_time){
            int start = convertToMinutes(slot[0]);
            int end = convertToMinutes(slot[1])+10;
            while (!pq.isEmpty() && pq.peek() <= start) {
                pq.poll();
            }             
        
            pq.add(end);
            maxRooms = Math.max(maxRooms, pq.size());
        }

        return maxRooms;
    }
    private static int convertToMinutes(String time) {
        String[] parts = time.split(":");
        int hours = Integer.parseInt(parts[0]);
        int minutes = Integer.parseInt(parts[1]);
        return hours * 60 + minutes;
    }
}
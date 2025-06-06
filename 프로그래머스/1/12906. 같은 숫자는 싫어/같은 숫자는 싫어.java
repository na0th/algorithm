import java.util.*;

public class Solution {
    public int[] solution(int[] arr) {
        Deque<Integer> deque = new ArrayDeque<>();
        
        int curNum = -1;
        for(int num : arr){
            if(curNum==-1){
                curNum = num;
                deque.addLast(curNum);
                continue;
            }
            if(curNum != num){
                curNum = num;
                deque.addLast(curNum);
            }
        }
        int[] answer = deque.stream()
                            .mapToInt(i->i)
                            .toArray();
                          

        return answer;
    }
}
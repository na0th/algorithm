import java.util.*;

class Solution {
    public int[] solution(String[] operations) {
        int[] answer;
        
        Deque<Integer> deque = new ArrayDeque<>();
        
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        
        StringTokenizer st;
        
        for (String operation : operations) {
            st = new StringTokenizer(operation);
            
            String op = st.nextToken();
            int number = Integer.parseInt(st.nextToken());
            
            if (op.equals("I")) {
                if (deque.isEmpty()) {
                    deque.add(number);
                    
                    max = number;
                    min = number;
                    
                    continue;
                }
                if (number <= min) {
                    deque.addFirst(number);
                    min = number;
                    continue;
                }
                if (number >= max) {
                    deque.addLast(number);
                    max = number;
                    continue;
                }
            } else {
                if (deque.isEmpty()) {
                    continue;
                }
                if (number == -1) {
                    deque.removeFirst();
                    
                    if (!deque.isEmpty()) {
                         min = deque.peekFirst();
                    } else {
                        min = Integer.MAX_VALUE;
                    }
                    
                    continue;
                }
                if (number == 1) {
                    deque.removeLast();
                    
                    if (!deque.isEmpty()) {
                        max = deque.peekLast();
                    } else {
                        max = Integer.MIN_VALUE;
                    }
                    continue;
                }
            }
        }
        
        if (deque.isEmpty()) {
                return new int[]{0, 0};
        }
        
        return new int[]{max, min};
    }
}
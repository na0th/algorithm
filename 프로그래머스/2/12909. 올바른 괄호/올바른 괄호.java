import java.util.*;
class Solution {
    boolean solution(String s) {
        boolean answer = true;
        
        Deque<Character> deque = new ArrayDeque<>();
        
        if (s.length() % 2 == 1) {
            return false;
        }
        
        for(int i=0; i<s.length(); i++){
            char c = s.charAt(i);
            
            if(c == '('){
                deque.addFirst(c);
            }
            else{
                if (deque.isEmpty() || deque.peekFirst() != '(') {
                    return false;
                }
                deque.removeFirst();
            }
        }

        return deque.isEmpty();
    }
}
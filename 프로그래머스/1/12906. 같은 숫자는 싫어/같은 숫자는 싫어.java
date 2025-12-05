import java.util.*;

public class Solution {
    /*
    arr = [1,1,3,3,0,1,1]이면
    분류 : 스택
    어떻게 풀이?
    1. 맨 처음 배열의 숫자를 스택에 넣는다.
    2. 그 이후부터는 스택의 맨 위 숫자와 같으면 무시하고, 다르면 넣는다
    
    */
    public int[] solution(int []arr) {
        Deque<Integer> st = new ArrayDeque<>();
        
        for (int x : arr) {
            if (st.isEmpty() || st.peekLast() != x) {
                st.addLast(x);
            }
        }
        
        int[] answer = st.stream()
              .mapToInt(x->x)
              .toArray();

        return answer;
    }
}
import java.util.*;
class Solution {
    /*
    초 단위로 기록된 주식 가격이 있음.
    가격이 떨어지지 않은 기간이 몇초인지 return
    
    알고리즘 분류 : 
    먼저 들어온게 뭔가 나중에 나가는 느낌이 있어? 스택
    어떻게 풀이?
    1.[price,초] 이렇게 만들어서 스택에 담아
    2.순차 탐색하면서 스택 맨 위 vs 순차 탐색 하는 놈 비교
    3. 순차 탐색이 더 크다? 그럼 answer[t] = i-t, 
    4. 마지막까지 안됐다.. 그럼 price 크기 - t 추가..
    */
    public int[] solution(int[] prices) {
        Deque<int[]> stack = new ArrayDeque<>();
        int n = prices.length;
        
        int[] answer = new int[n];
        //문제는 [price,초] 이거는 Deque에 안되나? 됨
        
        for(int i=0; i<prices.length; i++){
            while(!stack.isEmpty() && stack.peekFirst()[0] > prices[i]){
                int[] pop = stack.removeFirst();
                answer[pop[1]] = i-pop[1];  
            }
            stack.addFirst(new int[]{prices[i],i});
        }
        while(!stack.isEmpty()){
            int[] pop = stack.removeFirst();
            answer[pop[1]] = n-1-pop[1];
        }
        // System.out.println(Arrays.toString(answer));
        
        // for (int[] element : stack) {
        //     System.out.print(Arrays.toString(element));
        // }
        
        return answer;
    }
}
import java.util.*;
import java.io.*;
import java.util.stream.*;
class Solution {
    /*
    1.queue1과 queue2의 sum을 비교한다.
    2.작은 쪽에서 큰 쪽으로 수를 넘긴다.
    3. cnt++ 한다.
    
    다시 1번..
    
    
    */
    public int solution(int[] queue1, int[] queue2) {
        List<Integer> list1 = Arrays.stream(queue1)
            .boxed()
            .collect(Collectors.toList());
        List<Integer> list2 = Arrays.stream(queue2)
            .boxed()
            .collect(Collectors.toList());
        Deque<Integer> deque1 = new ArrayDeque<>(list1);
        Deque<Integer> deque2 = new ArrayDeque<>(list2);
        
        long sum1 = 0L;
        long sum2 = 0L;
        sum1 = list1.stream()
            .mapToInt(Integer::intValue)
            .sum();
        sum2 = list2.stream()
            .mapToInt(Integer::intValue)
            .sum();
        
        int size = 4 * queue1.length;
        
        
        if (sum1 == sum2 ){return 0;}
        int num1 = 0;
        int num2 = 0;
        int cnt = 0 ;
        
        while(cnt <= size && !deque1.isEmpty() && !deque2.isEmpty()){
            num1 = deque1.peekFirst();
            num2 = deque2.peekFirst();
            
            if(sum1>sum2){
                deque2.addLast(deque1.removeFirst());
                sum1-=num1;
                sum2+=num1;
            }else{
                deque1.addLast(deque2.removeFirst());
                sum1+=num2;
                sum2-=num2;
            }
            cnt++;
            if(sum1==sum2){
                return cnt;
            }
            
        }
        return -1;
    }
}
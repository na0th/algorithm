import java.util.*;
import java.io.*;
import java.util.stream.*;
import java.lang.Math;
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> proList = Arrays.stream(progresses)
                .boxed()
                .collect(Collectors.toList());
        
        Deque<Integer> deque = new ArrayDeque<>();
        
        for(int i=0; i<progresses.length;i++){
            int task = calculateDays(progresses[i],speeds[i]);
            System.out.println(task);
            deque.offer(task);
        }
        List<Integer> result = new ArrayList<>();
        
            while(!deque.isEmpty()){
                int first = deque.poll();
                int count = 1;
                
                while (!deque.isEmpty() && deque.peek() <= first) {
                    deque.poll();
                    count++;
                }
                result.add(count);
            }
        return result.stream().mapToInt(Integer::intValue).toArray();
    }
    private static int calculateDays(int progress,int speed){
        int task = (100-progress)/speed;
        if(speed!=1){
            task+=1;
        }
        return task;
        // return (int) Math.ceil((100.0 - progress) / speed);
    }  
}
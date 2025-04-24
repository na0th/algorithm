import java.util.*;
class Solution {
    /*
    배열의 i번째부터 j번째 까지 자른다
    그걸 정렬한다
    k번째 수를 리턴한다
    
    알고리즘 분류 : 정렬
    어떻게 풀이? 그냥 그대로 구현
    */
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        for(int i=0; i<commands.length;i++){
            int[] command = commands[i];
            List<Integer> row = new ArrayList<>();
            for(int p = command[0]-1; p<command[1]; p++){
                row.add(array[p]);
            }
            Collections.sort(row);
            answer[i] = row.get(command[2]-1);
        }
        
        return answer;
    }
}
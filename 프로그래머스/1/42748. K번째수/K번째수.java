import java.util.*;
import java.util.stream.*;
class Solution {
    /*
    배열 array의 i~j번째 자르고 정렬했을 때, k번째 수 구하기
    분류 : 단순 구현, 정렬?
    어떻게 풀이?
    1. 배열을 자른다
    2. 정렬한다
    */
    public int[] solution(int[] array, int[][] commands) {
        List<Integer> list = Arrays.stream(array)
                                   .boxed()
                                   .collect(Collectors.toList());
        List<Integer> answerList = new ArrayList<>();
        for(int i=0; i<commands.length; i++){
            int[] command = commands[i];
            int start = command[0]-1;
            int end = command[1];
            int k = command[2] - 1;
            
            List<Integer> sliceCopy = new ArrayList<>(list.subList(start, end));
            
            Collections.sort(sliceCopy);
            answerList.add(sliceCopy.get(k));
        }
        return answerList.stream()
            .mapToInt(x->x)
            .toArray();

    }
}
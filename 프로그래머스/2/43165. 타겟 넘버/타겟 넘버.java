import java.util.*;
class Solution {
    /**
    정수를 더하거나 빼서 타겟 넘버를 만들어야 한다.
    ! 순서 바꾸지 않기
    알고리즘 분류 : 완전탐색(DFS or BFS)
    어떻게 풀이 ? 
    DFS로 완전 탐색 -> 2^20이라 가능하다
    
    */
    static int targetCount = 0;
    public int solution(int[] numbers, int target) {
        dfs(numbers,0,0,target);
        
        return targetCount;
    }
    public void dfs(int[] numbers, int start,int depth,int target){
        if(depth>=numbers.length){
            if(target == 0){
                targetCount++;
            }
            return;
        }
        dfs(numbers,start+1,depth+1, target-numbers[start]);
        dfs(numbers,start+1,depth+1, target+numbers[start]);
        
    }
}
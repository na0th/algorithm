import java.util.*;
class Solution {
    /**
    0 -5 -4 1 0 -6 이고 최대 고도는 1이다..
    알고리즘 분류 :  구현?
    어떻게 풀이 ? 
    최대값이랑 현재 고도랑 게속 비교한다.
    리턴한다.
     */
    
    public int largestAltitude(int[] gain) {
        int max = 0;
        int current = 0;
        for(int h : gain){
            current+=h;
            if(max<current){
                max = current;
            }
        }
        return max;
    }
}
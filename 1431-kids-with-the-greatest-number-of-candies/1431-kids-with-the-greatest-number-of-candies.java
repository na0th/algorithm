import java.util.*;
import java.io.*;
import java.util.stream.*;
class Solution {
    /**
    extraCandies를 줬을 때, 해당 아이가 최대 캔디 해당자인지를 출력
    
    알고리즘 분류 : ? 
    어떻게 풀이 :
    array에서 최대 캔디 수를 구한다
    해당 아이 캔디 + extraCandies를 더한 후, 최대 캔디 수와 비교한다.
    최대 캔디 수보다, 여분 캔디를 더해도 작다면.. false
    크다면 .. true  
     */

    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int maxNum = Arrays.stream(candies)
            .max()
            .getAsInt();
        // int candySize = candies.length;
        // boolean[] result = new boolean[candySize];
        List<Boolean> result = new ArrayList<>();
        for(int candy : candies){
            if( (candy+extraCandies) >= maxNum){
                result.add(true);
            }else{
                result.add(false);
            }
        }

        return result;
    }
}
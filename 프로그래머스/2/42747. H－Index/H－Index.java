import java.util.*;
import java.util.stream.Collectors;
class Solution {
    public int solution(int[] citations) {
        /*
        문제 설명
        n편 논문 중, h편 이상 인용된 논문이 h편이상이고,
        나머지가 h편이하라면 h의 최대값이 h-index
        
        알고리즘 분류 : 정렬 
        어떻게 풀이? [3,0,6,1,5]
        [0,1,3,5,6]
        h가 0이면? 0이상 5, 0이하 1   0 이상, 0 이하 x
        h가 1이면? 1이상 4, 1이하 2  1 이상, 1이하 X
        h가 2이면? 2이상 3, 2이하 2  2이상, 2이하 
        h가 3이면? 3이상 3 , 3이하 3  == 최대
        h가 4이면? 4이상 2, 4이하 4
        
        정렬해놓고, n번 순회해보자
        */
        // List<Integer> arr = new ArrayList<>(Arrays.asList(citations)); 
        //int와 Integer간 타입 불일치로 안됨.. List는 참조형만 가능 원시 X
        
//         List<Integer> arr = Arrays.stream(citations)
//                     .boxed()
//                     .collect(Collectors.toList());
        
//         Collections.sort(arr);
//         for(int i=0; i<arr.size();i++){
//             //0,1,3,5,6
//             if(arr.get(i) >= arr.size()-i){
//                 return arr.size()-i;
//             }
//         }
//         int answer = 0;
//         return answer;
        
        Arrays.sort(citations);
        for(int i=0; i<citations.length;i++){
            //0,1,3,5,6
            if(citations[i] >= citations.length-i){
                return citations.length-i;
            }
        }
        return 0;


    }
}
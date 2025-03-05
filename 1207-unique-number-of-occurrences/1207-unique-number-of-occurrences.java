import java.util.*;
class Solution {
    /**
    각 값의 발생 횟수가 고유하다면 true, 고유하지 않으면 false

    알고리즘 분류 : 자료구조 Map,Set
    어떻게 풀이 : counting해서 k,v로 저장 
    그 value를 set으로 만들었을 때 size가 같으면 true, 아니면 false
     */
    public boolean uniqueOccurrences(int[] arr) {
        
        Map<Integer,Integer> map = new HashMap<>();

        for(int num : arr){
            map.put(num, map.getOrDefault(num,0)+1);
        }
        List<Integer> list = new ArrayList<>(map.values());
        Set<Integer> set = new HashSet<>(map.values());

        return set.size() == list.size();
    }
}
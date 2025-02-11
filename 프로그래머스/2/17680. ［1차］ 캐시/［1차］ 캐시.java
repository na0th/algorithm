import java.util.*;
import java.io.*;
class Solution {
    /*
    캐시 사이즈
    대소문자 구분 X
    캐시 교체 알고리즘은 LRU
    캐시 히트의 경우 실행 시간 1
    캐시 미스의 경우 실행 시간 5
    
    캐시 사이즈가 3보다 작다
    - 내가 있으면 히트
    - 내가 없으면 추가(5초)
    
    캐시 사이즈가 3이다
    - 내가 있으면 히트 
    - 내가 없으면 맨 앞에거 빼고 내꺼 추가(5초)
    
    알고리즘 분류 : 구현
    어떻게 풀이 ? 
    List<String> 꼴로 size를 계속 확인하며 따진다.
    */
    public int solution(int cacheSize, String[] cities) {
        if (cacheSize == 0) return cities.length * 5;
        Deque<String> cache = new ArrayDeque<>();
        int cnt = 0;
        
        for(String city : cities){
            city = city.toUpperCase();
             
            if(cache.contains(city)){
                cache.remove(city);
                cache.addLast(city);
                cnt+=1;
                
            }else{
                if(cache.size() == cacheSize){
                    cache.removeFirst();
                }
                cache.addLast(city);
                cnt+=5;
            }   
            
        }
        return cnt;
        
    }
}
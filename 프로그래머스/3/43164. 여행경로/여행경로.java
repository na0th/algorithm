import java.util.*;
class Solution {
    /*
    ICN에서 출발
    [a,b]는 a->b 가능
    가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로 return
    
    알고리즘 분류 : DFS 
    어떻게 풀이? 
    1. ICN : [ooo , ooo , ooo] 꼴로 저장해서 DFS
    2. 
    */
    List<String> route = new LinkedList<>();
    Map<String,PriorityQueue<String>> graph = new HashMap<>();

    public String[] solution(String[][] tickets) {
        for(String[] ticket : tickets){
            graph.computeIfAbsent(ticket[0], k -> new PriorityQueue<>()).add(ticket[1]);
        }
        
        dfs("ICN");
        return route.toArray(new String[0]);
    }
    public void dfs(String start){
        PriorityQueue<String> pq = graph.get(start);
        while(pq != null &&!pq.isEmpty() ){
            dfs(pq.poll());
        }
        route.add(0,start);
    }
}
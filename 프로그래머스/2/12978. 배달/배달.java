import java.util.*;
import java.io.*;
class Solution {
    /*
    양방향 도로, 1번마을에서 n개의 마을중 k 시간 이하로 배달이 가능한 마을에서만 주문.. 
    음식 주문을 받을 수 있는 마을의 개수를 return
    
    알고리즘 분류 : 그래프, 다익스트라 
    다익스트라인 이유는 1번 마을에서의 최소 거리(시간)을 찾는 것이기 때문이다.
    
    어떻게 풀이?
    우선순위큐에서 시간이 가장 적은 것을 뽑아서 최신화 시키고 다시 넣고 ....
    우선순위큐 모든 큐가 끝날 때까지 반복한 후에 결과 확인
    
    */
    final static int START = 0;
    public int solution(int N, int[][] road, int K) {


        Map<Integer, List<int[]>> graph = new HashMap<>();
        //graph 만들기
        for(int i=0; i<road.length; i++){
            int start = road[i][0];
            int end = road[i][1];
            int dist = road[i][2];
            
            graph.putIfAbsent(start, new ArrayList<>());
            graph.putIfAbsent(end, new ArrayList<>());
            
            graph.get(start).add(new int[]{end,dist});
            graph.get(end).add(new int[]{start,dist});
               
        }
        
        
        
        Map<Integer, Integer> costs = dijkstra(graph, 1);
        int cnt = 0;
        for (Map.Entry<Integer, Integer> entry : costs.entrySet()) {
            if (entry.getValue() <= K) {
                cnt++;
            }
        }
        return cnt;
        
    }
    private Map<Integer, Integer> dijkstra(Map<Integer, List<int[]>> graph, int start){
        Map<Integer , Integer> costs = new HashMap<>();
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        
        pq.add(new int[]{0, start});
        while(!pq.isEmpty()){
            int[] current = pq.poll();
            int curCost = current[0];
            int curNode = current[1];
            
            if(!costs.containsKey(curNode)){
                costs.put(curNode,curCost);
                
                if(graph.containsKey(curNode)){
                    for(int[] neighbor : graph.get(curNode)){
                    int nextNode = neighbor[0];
                    int nextCost = curCost+ neighbor[1];

                    pq.add(new int[]{nextCost,nextNode});
                    }
                }
                
            }
        }
        return costs;
    }
}
import java.util.*;
import java.io.*;
import java.lang.*;
class Solution {
    /*
    전력망 네트워크를 2개로 분할 할 때, 송전탑 개수의 차이의 최솟값을 구하시오.
    
    알고리즘 분류 : 완전탐색? dfs,bfs 
    어떻게 풀이 ? 
    첫 번째 원소부터 끊어본다..1,3 / 2,3 / 3,4 .. 면 [1,3]먼저 끊어본 다음([1,3]을 제외한다는 뜻)
    
    그다음 한쪽을 dfs로 다 합쳐서 길이를 재고, n개에서 뺀다.. 그 값을 전부 모아놓고 최솟값 계산
    
    */
    
    public int solution(int n, int[][] wires) {
        int minDiff = Integer.MAX_VALUE;
        
        for(int i =0; i<wires.length;i++){
            List<Integer>[] graph = new ArrayList[n+1];
            
            for (int k = 0; k <= n; k++) {
                graph[k] = new ArrayList<>();
            }
            
            Set<Integer> visited = new HashSet<>();
            
            for(int j=0; j<wires.length; j++){
                if (j==i) continue;
                addEdge(graph, wires[j][0], wires[j][1]);
            }
            
            dfs(graph, wires[i][0], visited);
            
            int count = visited.size();      // 한 네트워크의 노드 개수
            int diff = Math.abs(n - 2 * count); // 두 네트워크의 노드 개수 차이 계산
            
            minDiff = Math.min(minDiff, diff);
        }
        return minDiff;
        
        
    }
    public void addEdge(List<Integer>[] graph, int u, int v){
        graph[u].add(v);
        graph[v].add(u);
    }
    public void dfs(List<Integer>[] graph, int u, Set<Integer> visited){
        visited.add(u);
        
        for(int v : graph[u]){
            if(!visited.contains(v)){
                dfs(graph,v,visited);
            }
        }
    }
}
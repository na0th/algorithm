import java.util.*;
class Solution {
    /**
    0 ~ n-1의 방이 있다
    방 안에는 여러개의 키가 있다.
    키는 방을 열 수 잇다
    모든 방을 돌 수 있으면 true, 아니면 false 반환


    알고리즘 분류 : DFS
    어떻게 풀이 ? 
    0번방은 그냥 들어갈 수 있다.
    1)방에서 돌 수 있는 방을 모두 돈다.
    2)방문한 방들을 방문 처리
    3)다 돌았는데 방문 처리 안된 방 있으면 FALSE
    */
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        int n = rooms.size();
        Set<Integer> visited = new HashSet<>();

        //재귀
        dfs(0,visited,rooms);
        
        return visited.size() == rooms.size();
        
    }
    public void dfs(int currentRoom, Set<Integer> visited, List<List<Integer>> rooms){
        visited.add(currentRoom);
        for(int key : rooms.get(currentRoom)){
            if(!visited.contains(key)){
                dfs(key,visited,rooms); 
            }
            
        }
        
    }
}
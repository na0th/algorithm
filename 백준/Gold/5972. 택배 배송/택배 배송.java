import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    /*
    현서 -> 찬홍
    최소의 여물 -> 최소 거리

    알고리즘 분류 : 최소 거리니까 다익스트라?
    어떻게 풀이?
    첫 시작점에서 가능한 경로를 다 담는다.
    우선순위큐로 최소 거리에 있는 경우만 이동한다
    도착하면 끝낸다
    * */
    public static class Point{
        int curX;
        int cost;
        Point(int curX, int cost){
            this.curX = curX;
            this.cost = cost;
        }

    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] parts = br.readLine().split(" ");
        int n = Integer.parseInt(parts[0]);
        int m = Integer.parseInt(parts[1]);
        Map<Integer, List<Point>> map = new HashMap<>();
        for (int i = 0; i < m; i++) {
            String[] row = br.readLine().split(" ");
            int start = Integer.parseInt(row[0]);
            int end = Integer.parseInt(row[1]);
            int cost = Integer.parseInt(row[2]);

            //양방향 처리
            if (!map.containsKey(start)) {map.put(start, new ArrayList<>());}
            if (!map.containsKey(end)) {map.put(end, new ArrayList<>());}
            map.get(start).add(new Point(end, cost));
            map.get(end).add(new Point(start, cost));
        }
        PriorityQueue<Point> pq = new PriorityQueue<>(Comparator.comparingInt(p -> p.cost));

        int[] dist = new int[n + 1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        //초기값 세팅
        pq.add(new Point(1, 0));
        while (!pq.isEmpty()) {
            Point p = pq.poll();
            if (p.curX == n) {break;}
            List<Point> list = map.get(p.curX);
            for (Point next : list) {
                int newCost = p.cost + next.cost;
                if (newCost < dist[next.curX]) {
                    dist[next.curX] = newCost;
                    pq.add(new Point(next.curX, newCost));
                }
            }
        }
        System.out.print(dist[n]);
    }
}

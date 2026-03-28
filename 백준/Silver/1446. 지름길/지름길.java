import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static class Point {
        int x, cost;

        Point(int x, int cost) {
            this.x = x;
            this.cost = cost;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] parts = br.readLine().split(" ");
        int n = Integer.parseInt(parts[0]);
        int d = Integer.parseInt(parts[1]);

        HashMap<Integer, List<Point>> map = new HashMap<>();
        int[] dist = new int[d + 1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[0] = 0;

        //그래프 세팅
        for (int i = 0; i < n; i++) {
            String[] row = br.readLine().split(" ");
            int start = Integer.parseInt(row[0]);
            int end = Integer.parseInt(row[1]);
            int cost = Integer.parseInt(row[2]);
            if (!map.containsKey(start)) {
                map.put(start, new ArrayList<>());
            }
            // 무시 조건
            if (start > d || cost >= (end - start) || end > d) continue;
            map.get(start).add(new Point(end, cost));
        }
        PriorityQueue<Point> pq = new PriorityQueue<>(Comparator.comparingInt(o -> o.cost));
        pq.add(new Point(0, 0));
        while (!pq.isEmpty()) {
            // p는 누적, next는 curCost
            Point p = pq.poll();
            if (p.cost > dist[p.x]) continue;
            if (map.containsKey(p.x)) {
                List<Point> list = map.get(p.x);
                for (Point next : list) {
                    int newCost = p.cost + next.cost;
                    if (newCost < dist[next.x]) {
                        dist[next.x] = newCost;
                        pq.add(new Point(next.x, newCost));
                    }
                }
            }
            // p.x+1 <d => d보다는 작아야하고, dist의 다음 칸이 쭉 걸어간 것 보다는 작아야한다? => 중복제거
            if (p.x + 1 <= d && dist[p.x + 1] > p.cost + 1) {
                dist[p.x + 1] = p.cost + 1;
                pq.add(new Point(p.x + 1, dist[p.x + 1]));
            }

        }
        System.out.print(dist[d]);
    }
}

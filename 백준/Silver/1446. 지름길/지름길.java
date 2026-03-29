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

        for (int i = 0; i < n; i++) {
            String[] row = br.readLine().split(" ");
            int start = Integer.parseInt(row[0]);
            int end = Integer.parseInt(row[1]);
            int cost = Integer.parseInt(row[2]);
            if (!map.containsKey(start)) map.put(start, new ArrayList<>());
            if (cost > end - start || end > d) continue;
            map.get(start).add(new Point(end, cost));
        }


        PriorityQueue<Point> pq = new PriorityQueue<>((o1, o2) -> Integer.compare(o1.cost, o2.cost));
        pq.add(new Point(0, 0));

        while (!pq.isEmpty()) {
            Point p = pq.poll();
            // dist 값보다 큰 경우는 취급 안한다..
            if (p.cost > dist[p.x]) continue;
            List<Point> list = map.get(p.x);
            if (map.containsKey(p.x)) {
                for (Point next : list) {
                    //지름길 타는 경우 우선순위큐에 넣는다.
                    int newCost = p.cost + next.cost;
                    if (dist[next.x] > newCost) {
                        dist[next.x] = newCost;
                        pq.add(new Point(next.x, newCost));
                    }
                }
            }

            // 지름길 도착해도 안타는 경우도 존재, 만약 1칸 이동한 경우의 dist가 cost+1보다 클 경우에만 이동
            if (p.x + 1 <= d && dist[p.x + 1] > p.cost + 1) {
                dist[p.x + 1] = p.cost + 1;
                pq.add(new Point(p.x + 1, dist[p.x+1]));
            }
        }
        System.out.print(dist[d]);
    }
}

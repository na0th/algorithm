    import java.io.BufferedReader;
    import java.io.IOException;
    import java.io.InputStreamReader;
    import java.util.*;

    public class Main {
        /**/
        public static class Point {
            int x;
            int cost;
            Point(int x, int cost) {
                this.x = x;
                this.cost = cost;
            }
        }
        public static void main(String[] args) throws IOException {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            String[] parts = br.readLine().split(" ");
            int n = Integer.parseInt(parts[0]);
            int m = Integer.parseInt(parts[1]);

            HashMap<Integer, List<Point>> map = new HashMap<>();
            for (int i = 0; i < m; i++) {
                String[] part = br.readLine().split(" ");
                int start = Integer.parseInt(part[0]);
                int end = Integer.parseInt(part[1]);
                int cost = Integer.parseInt(part[2]);

                // 양방향
                if (!map.containsKey(start)) {map.put(start, new ArrayList<>());}
                if (!map.containsKey(end)) {map.put(end, new ArrayList<>());}
                map.get(start).add(new Point(end, cost));
                map.get(end).add(new Point(start, cost));
            }

            int[] dist = new int[n+1];
            Arrays.fill(dist, Integer.MAX_VALUE);

            PriorityQueue<Point> pq = new PriorityQueue<>(Comparator.comparingInt((Point p) -> p.cost));
            pq.add(new Point(1, 0));
            while (!pq.isEmpty()) {
                Point p = pq.poll();
                if (p.x == n) { break;}
                for (Point next : map.get(p.x)) {
                    int newCost = p.cost + next.cost;
                    if (newCost < dist[next.x] ) {
                        dist[next.x] = newCost;
                        pq.add(new Point(next.x, newCost));
                    }
                }
            }
            System.out.print(dist[n]);

        }
    }

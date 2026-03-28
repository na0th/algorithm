import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    /*
    고속도로에 지름길이 존재한다
    지름길은 일방통행이고, 역주행할 수 없다.
    운전해야 하는 거리의 최솟값 구하시오

    첫 째줄에 지름길의 개수 N, 고속도로의 길이 D가 주어진다
    N은 12이하, D는 10000이하 자연수
    다음 N개의 줄에는 지름길 시작 위치, 도착 위치, 지름길의 길이가 주어진다.

    알고리즘 분류 : 1칸씩 이동해보면서 최소 거리를 찾는 bfs ?
    어떻게 풀이?
        지름길에 없으면 cost+1
        지름길에 있으면 cost+1, 지름길 이동한 cost를 경우의 수를 둘 다 추가
        지름길 이동한 경우 새로운 cost가 더 짧다면 dist에 업데이트
        우선순위큐로 cost가 짧은 애들 먼저 뽑기
        도착 위치에 도착하면 끝이 아니고, 다 끝난 다음 dist[n] 출력?

        모르겠음. 일단 진행
    * */
    public static class Point {
        int x;
        int cost;
        Point(int x, int cost) {
            this. x=  x;
            this.cost = cost;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] parts = br.readLine().split(" ");
        int n = Integer.parseInt(parts[0]);
        int d = Integer.parseInt(parts[1]);
        //같은 출발, 도착지점이라면 dist가 짧은 것만 넣기
        HashMap<Integer, List<Point>> map = new HashMap<>();

        int[] dist = new int [d+1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[0] = 0;
        //기본적으로는 1칸당 1세팅

        for (int i = 0; i < n; i++) {
            String[] row = br.readLine().split(" ");
            int start = Integer.parseInt(row[0]);
            int end = Integer.parseInt(row[1]);
            int cost = Integer.parseInt(row[2]);
            if (!map.containsKey(start)) {
                map.put(start, new ArrayList<>());
            }
            //제외조건
            if (end > d || cost >= (end - start) || start > d) {continue;}
            map.get(start).add(new Point(end, cost));
        }
        //지름길에 도착한 경우는 경우의수를 2개 추가. 지름길 이동, 그냥 이동
        PriorityQueue<Point> pq = new PriorityQueue<>(Comparator.comparingInt((Point p) -> p.cost));
        pq.add(new Point(0,  0));
        while (!pq.isEmpty()) {
            Point p = pq.poll();
            if (p.cost > dist[p.x]) continue;
            if (map.containsKey(p.x)) {
                //해당 지름길
                List<Point> shortList = map.get(p.x);
                //END로 이동 후,
                for (Point shortP : shortList) {
                    int newCost = p.cost + shortP.cost;
                    if (dist[shortP.x] > newCost) {
                        dist[shortP.x] = newCost;
                        pq.add(new Point(shortP.x, newCost));
                    }
                }
            }
            //중복 안 생기도록 cost보다 작으면 그냥 넘어가야겟다.  일단보류
            if (p.x +1 <= d && dist[p.x + 1] > p.cost + 1) {
                dist[p.x + 1] = p.cost + 1;
                pq.add(new Point((p.x) + 1, p.cost + 1));
            }
        }
        System.out.print(dist[d]);

    }
}
